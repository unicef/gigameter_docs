"""
Tajik translation pipeline for the Giga Meter docs.

GitBook's computed translation does not support Tajik, so this script maintains
a repo-based mirror: it translates the school-facing English pages into tj/
using Claude, guided by .github/translation-prompt-tg.md and
.github/translation-glossary-tg.csv.

Two modes per page:
- SEED: no Tajik file exists yet -> full translation from English.
- PATCH: a Tajik file exists (possibly human-polished) -> Claude receives the
  previous English snapshot, the new English, and the current Tajik, and applies
  only the changes that correspond to the English edit. Existing Tajik phrasing
  is preserved verbatim everywhere else, so human polish is never regenerated.

The English snapshot each translation was made from is kept in
tj/.en-snapshots/. Drift detection: sha256 of each English source is stored in
tj/.translation-state.json. The workflow opens a PR with the result — Tajik
output is always human-reviewed before merge.

Usage:
    ANTHROPIC_API_KEY=<key> python translate_tj.py [--force-seed] [--only <en_path>]

--force-seed re-translates pages from scratch, DISCARDING existing Tajik
content (including human polish). Only use it before the seed is reviewed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

import anthropic

# English source → Tajik target. Full site except README.md — its stats and
# release blocks change daily via automation, which would generate a PR per day;
# tj/README.md is a hand-maintained landing page instead.
PAGES: dict[str, str] = {
    "docs/getting-started/overview.md": "tj/overview.md",
    "docs/getting-started/features.md": "tj/features.md",
    "docs/deployment/case-studies.md": "tj/case-studies.md",
    "get-started/metric-glossary.md": "tj/metric-glossary.md",
    "get-started/faq.md": "tj/faq.md",
    "docs/installation/system-requirements.md": "tj/system-requirements.md",
    "docs/installation/installation-guide.md": "tj/installation-guide.md",
    "docs/troubleshooting/troubleshooting.md": "tj/troubleshooting.md",
    "docs/deployment/government-onboarding-overview.md": "tj/government-onboarding-overview.md",
    "docs/deployment/deployment-blueprint.md": "tj/deployment-blueprint.md",
    "docs/deployment/installation-lead.md": "tj/installation-lead.md",
    "docs/deployment/data-analysis-lead.md": "tj/data-analysis-lead.md",
    "country-deployment/using-the-dashboard.md": "tj/using-the-dashboard.md",
    "docs/deployment/deployment-checklist.md": "tj/deployment-checklist.md",
    "docs/security/privacy-and-security.md": "tj/privacy-and-security.md",
    "technical-reference/network-destinations.md": "tj/network-destinations.md",
    "docs/technical-reference/self-hosting.md": "tj/self-hosting.md",
    "docs/technical-reference/self-hosting/installation.md": "tj/self-hosting/installation.md",
    "docs/technical-reference/self-hosting/docker.md": "tj/self-hosting/docker.md",
    "docs/technical-reference/self-hosting/windows-app.md": "tj/self-hosting/windows-app.md",
    "docs/technical-reference/self-hosting/unit-testing.md": "tj/self-hosting/unit-testing.md",
    "docs/technical-reference/self-hosting/dev-skillset.md": "tj/self-hosting/dev-skillset.md",
    "docs/technical-reference/self-hosting/infra-requirements.md": "tj/self-hosting/infra-requirements.md",
    "docs/technical-reference/api-reference.md": "tj/api-reference.md",
    "docs/technical-reference/measurement-protocols.md": "tj/measurement-protocols.md",
    "docs/technical-reference/internet-measurement-101.md": "tj/internet-measurement-101.md",
}

PROMPT_PATH = Path(".github/translation-prompt-tg.md")
GLOSSARY_PATH = Path(".github/translation-glossary-tg.csv")
STATE_PATH = Path("tj/.translation-state.json")
SNAPSHOT_DIR = Path("tj/.en-snapshots")

MODEL = "claude-sonnet-5"

PATCH_INSTRUCTIONS = """\
You are UPDATING an existing, human-reviewed Tajik translation, not retranslating.

You will receive:
1. PREVIOUS ENGLISH — the English source the current Tajik was translated from
2. NEW ENGLISH — the current English source
3. CURRENT TAJIK — the existing translation, which contains human corrections

Rules:
- Identify what changed between PREVIOUS ENGLISH and NEW ENGLISH.
- Apply ONLY the corresponding changes to CURRENT TAJIK.
- Every sentence of CURRENT TAJIK that corresponds to unchanged English must be
  preserved VERBATIM — do not rephrase, "improve", or re-translate it. The
  existing wording carries human review and takes precedence over your own
  preferences and over this prompt's phrasing rules.
- New or changed passages are translated per the instructions above, matching
  the terminology and register already used in CURRENT TAJIK.
- Return ONLY the full updated Tajik markdown document."""


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {}


def snapshot_path(en_path: str) -> Path:
    return SNAPSHOT_DIR / en_path.replace("/", "__")


def build_system_prompt() -> str:
    prompt = PROMPT_PATH.read_text()
    glossary = GLOSSARY_PATH.read_text()
    return (
        f"{prompt}\n\n"
        f"## Glossary (en,tg) — apply exactly\n\n```csv\n{glossary}\n```\n\n"
        "Return ONLY the translated markdown document — no preamble, no code fences "
        "around the whole document, no explanation."
    )


def response_text(message) -> str:
    text = "".join(b.text for b in message.content if b.type == "text")
    return text.strip() + "\n"


def seed_translate(client: anthropic.Anthropic, system: str, en_text: str) -> str:
    message = client.messages.create(
        model=MODEL,
        max_tokens=32000,
        system=system,
        messages=[
            {
                "role": "user",
                "content": (
                    "Translate this Giga Meter documentation page from English "
                    f"to Tajik per your instructions:\n\n{en_text}"
                ),
            }
        ],
    )
    return response_text(message)


def patch_translate(
    client: anthropic.Anthropic,
    system: str,
    old_en: str,
    new_en: str,
    current_tj: str,
) -> str:
    message = client.messages.create(
        model=MODEL,
        max_tokens=32000,
        system=f"{system}\n\n{PATCH_INSTRUCTIONS}",
        messages=[
            {
                "role": "user",
                "content": (
                    f"PREVIOUS ENGLISH:\n\n{old_en}\n\n---\n\n"
                    f"NEW ENGLISH:\n\n{new_en}\n\n---\n\n"
                    f"CURRENT TAJIK:\n\n{current_tj}"
                ),
            }
        ],
    )
    return response_text(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--force-seed",
        action="store_true",
        help="re-translate every page from scratch, discarding existing Tajik",
    )
    parser.add_argument("--only", help="translate a single English source path")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)
    client = anthropic.Anthropic(api_key=api_key)

    system = build_system_prompt()
    config_hash = sha256(system)

    state = load_state()
    # Prompt/glossary changes re-seed only pages that have never been
    # human-touched; for existing pages they apply to future patches instead
    # of triggering a destructive full re-translation.
    stale_config = state.get("_config") != config_hash

    pages = PAGES
    if args.only:
        if args.only not in PAGES:
            print(f"ERROR: {args.only} is not a tracked page", file=sys.stderr)
            sys.exit(1)
        pages = {args.only: PAGES[args.only]}

    changed = 0
    for en_path, tj_path in pages.items():
        en_file, tj_file = Path(en_path), Path(tj_path)
        if not en_file.exists():
            print(f"SKIP {en_path}: source missing")
            continue
        en_text = en_file.read_text()
        en_hash = sha256(en_text)
        snap_file = snapshot_path(en_path)

        if state.get(en_path) == en_hash and tj_file.exists() and not args.force_seed:
            print(f"OK    {en_path}: unchanged")
            continue

        tj_file.parent.mkdir(parents=True, exist_ok=True)
        if tj_file.exists() and snap_file.exists() and not args.force_seed:
            print(f"PATCH {en_path} -> {tj_path} ...")
            tj_file.write_text(
                patch_translate(
                    client, system, snap_file.read_text(), en_text, tj_file.read_text()
                )
            )
        else:
            print(f"SEED  {en_path} -> {tj_path} ...")
            tj_file.write_text(seed_translate(client, system, en_text))

        snap_file.parent.mkdir(parents=True, exist_ok=True)
        snap_file.write_text(en_text)
        state[en_path] = en_hash
        changed += 1

    state["_config"] = config_hash
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n")
    print(f"Done: {changed} page(s) updated.")


if __name__ == "__main__":
    main()
