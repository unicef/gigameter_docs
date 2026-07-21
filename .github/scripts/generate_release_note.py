"""
Release note generator for giga-meter-docs README.md.

Takes a version, date, and raw changelog bullets, calls Claude to generate
polished prose in the established Giga Meter release note style, and writes
the result into the <!-- release-start --> / <!-- release-end --> block in README.md.

Usage:
    ANTHROPIC_API_KEY=<key> python generate_release_note.py \
        --version 2.1.0 \
        --date 2026-09-01 \
        --changes "faster speed tests" "offline mode" "French language support"

    Or pipe bullets from stdin:
    echo "faster speed tests\noffline mode" | python generate_release_note.py \
        --version 2.1.0 --date 2026-09-01
"""

import argparse
import os
import re
import sys

import anthropic

README_PATH = "README.md"

STYLE_PROMPT = """\
You write release notes for Giga Meter, a desktop app that monitors school internet quality.

Style rules:
- Start with "Giga Meter can now" — user-benefit framing, not a changelog list
- Two sentences maximum: lead with the headline user-facing changes, close with secondary improvements if any
- Conversational but precise — no marketing superlatives, no jargon
- Do not list every change mechanically; weave them into natural prose

Good example:
"Giga Meter can now measure internet speed more accurately and pinpoint your location automatically to provide better connectivity data. The app is also now available in Mongolian."

Bad example (do not do this):
"Version 2.0.3 improves speed-measurement accuracy, adds automatic location detection, adds Mongolian language support, and moves software updates to signed distribution."

Return only the prose — no preamble, no quotes, no explanation.\
"""


def generate_prose(version: str, changes: list[str]) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    bullet_list = "\n".join(f"- {c}" for c in changes)
    user_message = f"Write the release note body for Giga Meter {version}. Changes:\n{bullet_list}"

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=256,
        system=STYLE_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )
    return message.content[0].text.strip()


def update_readme(version: str, date: str, prose: str) -> None:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    block = (
        f"<!-- release-start:v{version} -->\n"
        f"{{% hint style=\"info\" %}}\n"
        f"**Giga Meter {version} — {date}**\n\n"
        f"{prose}\n\n"
        f"[Full release notes →](https://github.com/unicef/project-connect-daily-check-app/releases/tag/v{version})\n"
        f"{{% endhint %}}\n"
        f"<!-- release-end -->"
    )

    updated = re.sub(
        r"<!-- release-start:.*?-->.*?<!-- release-end -->",
        block,
        content,
        flags=re.DOTALL,
    )

    if updated == content:
        print("WARNING: release block markers not found in README — no changes written.")
        sys.exit(1)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"README updated with release note for v{version}.")
    print(f"\nGenerated prose:\n{prose}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a Giga Meter release note and update README.md")
    parser.add_argument("--version", required=True, help="Release version, e.g. 2.1.0")
    parser.add_argument("--date", required=True, help="Release date, e.g. 2026-09-01")
    parser.add_argument("--changes", nargs="*", default=[], help="List of changes (one per arg)")
    args = parser.parse_args()

    changes = args.changes
    if not changes and not sys.stdin.isatty():
        changes = [line.strip() for line in sys.stdin if line.strip()]

    if not changes:
        print("ERROR: provide at least one change via --changes or stdin", file=sys.stderr)
        sys.exit(1)

    print(f"Generating release note for v{args.version}...")
    prose = generate_prose(args.version, changes)
    update_readme(args.version, args.date, prose)


if __name__ == "__main__":
    main()
