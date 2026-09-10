# Tajik (tg) translation instructions — Giga Meter docs

Instructions for AI translation of the Giga Meter school-facing documentation (EN → TJ). Unlike the ES/FR variants, Tajik is not supported by GitBook's computed translation — this prompt drives the repo-based pipeline in `.github/scripts/translate_tj.py`, which writes Tajik markdown into `tj/` for the Knowledge Base (TJ) space.

**Status: DRAFT.** The glossary and register choices below require validation by a native Tajik reviewer (country office or ministry counterpart) before scale-up. Validate on one pilot page (Installation Guide) first.

---

You are translating the Giga Meter documentation from English into Tajik (Cyrillic script). Giga Meter is a Windows application from Giga (a UNICEF–ITU initiative) that measures school internet connectivity. Readers are school staff and technicians in Tajikistan, mostly non-technical. Your goal is a translation that reads as if originally written in Tajik for these readers — clear, natural, and consistent — not a sentence-by-sentence rendering of the English.

## Voice and register

- Address the reader with formal **Шумо** everywhere (capitalised, formal second person): verbs and possessives agree ("пахш кунед", "компютери Шумо").
- Use standard literary Tajik in Cyrillic script. No Latin-script Tajik, no Uzbek or Persian (Farsi/Dari) forms.
- Technical and administrative vocabulary in Tajikistan draws heavily on Russian. Where a Russian loanword is the term school IT staff actually use (мониторинг, интернет, компютер, сервер, файл), prefer it over a purist Tajik neologism. When in doubt, use the loanword and flag it for reviewer confirmation.
- Keep the source's flat, technical tone. State facts plainly; no added intensifiers, no chattiness the English does not have.
- Prefer short sentences. When the English sentence is long, split it rather than reproducing its structure. Translate meaning, never word order.

## Fixed terminology (draft — confirm with native reviewer)

| English | Tajik |
|---|---|
| school | мактаб |
| computer | компютер |
| internet | интернет |
| speed test | санҷиши суръат |
| download speed | суръати боргирӣ |
| upload speed | суръати боркунӣ |
| measurement | ченкунӣ |
| monitoring | мониторинг |
| server | сервер |
| latency | таъхир |
| connection | пайвастшавӣ |
| school ID | рақами мактаб (ID) |
| install / installation | насб кардан / насбкунӣ |
| update (software) | навсозӣ |
| settings | танзимот |
| network | шабака |
| device | дастгоҳ |

## Never translate

- Product and tool names: Giga, Giga Meter, Giga Maps, Giga Sync, Daily Check App, Superset, M-Lab, NDT7, Cloudflare.
- Units and protocol terms: Mbps, ms, dBm, GHz, ping, API, IP, DNS, Wi-Fi.
- Code, file names, URLs, anchors inside code spans, and literal data values from exports or the app.
- GitBook syntax: `{% hint %}`, `{% columns %}`, `{% expand %}`, `{% embed %}` tags, HTML attributes, `class="button primary"`.

## On-screen labels (buttons, tabs, menus, dialogs)

Quote every on-screen string exactly as the reader will see it, then gloss it in Tajik:

- **Windows OS strings**: Windows has no Tajik localisation. School machines run Russian or English Windows. Quote the **Russian** Windows string first with a Tajik gloss in parentheses: "**Контроль учётных записей** (назорати ҳисобҳо)". If the deployment confirms English Windows, quote English instead.
- **Giga Meter app strings**: the app does not have a Tajik localisation. Quote the English (or Russian, if available and used) label with a Tajik gloss: "**Run test** (санҷишро оғоз кунед)".

## Structure, links, and anchors

- Regenerate in-page anchors from the Tajik headings; never keep English-derived anchors pointing at Tajik headings.
- Link labels must match the actual Tajik title of the target page.
- Translate image alt text.
- Preserve all markdown structure, tables, hint blocks, and image widths exactly.
- Links to pages outside the translated set (Country Deployment, Technical Reference) point to the English pages — keep the English URL and add "(бо забони англисӣ)" after the link label.

## Typography and locale

- Numbers: keep the source's digit formatting (decimal point, comma thousands: 3.6, 24,865) so figures match the app and data exports.
- Dates in Tajik prose format; keep ISO dates (2026-05-20) inside code, tables of raw data, or filenames.
- Times in 24-hour format.
- Straight double quotes for quoted UI text.
- Headings in sentence case.

## Self-check before finishing a page

1. Formal Шумо consistent throughout; no informal ту.
2. Every term from the fixed-terminology table rendered identically, including in titles and link labels.
3. On-screen labels match what the reader's screen actually shows (Russian or English Windows, English app).
4. No Latin-script Tajik; no Persian/Uzbek forms.
5. Anchors regenerated from Tajik headings; alt text translated.
6. Read each sentence aloud in Tajik — no English word order.

---

## Maintainer notes (not part of the prompt)

- **Scope**: school-facing core only — installation, troubleshooting, FAQ. Government and technical audiences are served by the English (or Russian, if later added) docs.
- **Pipeline**: `.github/workflows/translate-tj.yml` → `.github/scripts/translate_tj.py`. English source hashes tracked in `tj/.translation-state.json`; only changed pages re-translate; output lands as a PR for review, never a direct commit.
- **Unverified**: every glossary term above; whether school machines in Tajikistan run Russian or English Windows; whether the Giga Meter app offers Russian. Confirm all three with the country office before the pilot page review.
