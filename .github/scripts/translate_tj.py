"""
Tajik translation pipeline for the Giga Meter docs.

GitBook's computed translation does not support Tajik, so this script maintains
a repo-based mirror: it translates the school-facing English pages into tj/
using Claude, guided by .github/translation-prompt-tg.md and
.github/translation-glossary-tg.csv.

Drift detection: sha256 of each English source is stored in
tj/.translation-state.json. Only pages whose source changed (or whose
translation is missing) are re-translated. The workflow opens a PR with the
result — Tajik output is always human-reviewed before merge.

Usage:
    ANTHROPIC_API_KEY=<key> python translate_tj.py [--force] [--only <en_path>]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

import anthropic

# English source → Tajik target. School-facing core only.
PAGES: dict[str, str] = {
    "docs/installation/system-requirements.md": "tj/system-requirements.md",
    "docs/installation/installation-guide.md": "tj/installation-guide.md",
    "docs/troubleshooting/troubleshooting.md": "tj/troubleshooting.md",
    "get-started/faq.md": "tj/faq.md",
}

PROMPT_PATH = Path(".github/translation-prompt-tg.md")
GLOSSARY_PATH = Path(".github/translation-glossary-tg.csv")
STATE_PATH = Path("tj/.translation-state.json")

MODEL = "claude-sonnet-5"


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {}


def build_system_prompt() -> str:
    prompt = PROMPT_PATH.read_text()
    glossary = GLOSSARY_PATH.read_text()
    return (
        f"{prompt}\n\n"
        f"## Glossary (en,tg) — apply exactly\n\n```csv\n{glossary}\n```\n\n"
        "Return ONLY the translated markdown document — no preamble, no code fences "
        "around the whole document, no explanation."
    )


def translate(client: anthropic.Anthropic, system: str, en_text: str) -> str:
    message = client.messages.create(
        model=MODEL,
        max_tokens=16384,
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
    return message.content[0].text.strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="re-translate every page")
    parser.add_argument("--only", help="translate a single English source path")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)
    client = anthropic.Anthropic(api_key=api_key)

    system = build_system_prompt()
    # Prompt or glossary changes invalidate every translation.
    config_hash = sha256(system)

    state = load_state()
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
        up_to_date = (
            state.get(en_path) == en_hash and tj_file.exists() and not stale_config
        )
        if up_to_date and not args.force:
            print(f"OK   {en_path}: unchanged")
            continue

        print(f"TRANSLATING {en_path} -> {tj_path} ...")
        tj_file.parent.mkdir(parents=True, exist_ok=True)
        tj_file.write_text(translate(client, system, en_text))
        state[en_path] = en_hash
        changed += 1

    state["_config"] = config_hash
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n")
    print(f"Done: {changed} page(s) translated.")


if __name__ == "__main__":
    main()
