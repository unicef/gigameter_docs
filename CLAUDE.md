# Giga Meter Knowledge Base — AI Instructions

This repo is the GitBook documentation site for **Giga Meter**, synced to GitHub at `unicef/gigameter_docs`. Content is written in GitHub-flavoured Markdown with GitBook block syntax (`{% hint %}`, `{% columns %}`, `{% expand %}`, `{% embed %}`). `SUMMARY.md` controls the sidebar; only files listed there are published.

---

## Before writing any documentation

Read `.github/tone-guide.md` in full before drafting, editing, or reviewing any page. It is the style standard for this knowledge base and must be followed without exception.

The one-paragraph brief from that guide (section 9 — paste this into your working context):

> Write in a flat, technical, mechanism-first register modelled on perfSONAR documentation and Kentik's Kentipedia. State facts plainly and let them carry the weight; explain how things work and why they behave that way. No marketing voice: no rule-of-three pitch fragments, no aphorisms or mission slogans, no chipper filler, no empty intensifiers (powerful/seamless/easy), no quantities that aren't grounded in real data. Tie operational content to decisions (what triggers a review, who acts, what happens). State constraints with their reason. Hedge precisely, not vaguely. Use tables for anything enumerable and callout blocks for out-of-band notes. Match depth to audience (school staff / government / technical) without getting chatty. Above all, never let the confident voice outrun the facts: verify authoritative-sounding claims harder, and ground every added statement in a real source. No emoji, no en dashes.

---

## Repo structure

```
README.md                        ← Introduction page (GitBook renders this as the homepage)
SUMMARY.md                       ← Sidebar navigation — controls what gets published
docs/
  getting-started/               ← overview.md, features.md
  installation/                  ← system-requirements.md, installation-guide.md
  troubleshooting/               ← troubleshooting.md, faq.md
  data/                          ← metric-glossary.md
  deployment/                    ← government-onboarding-overview.md, deployment-blueprint.md,
                                    installation-lead.md, data-analysis-lead.md,
                                    deployment-checklist.md, case-studies.md
  technical-reference/           ← data-governance.md, api-reference.md,
                                    measurement-protocols.md, internet-measurement-101.md,
                                    self-hosting.md + self-hosting/ (sub-pages)
docs/security/                   ← privacy-and-security.md
technical-reference/             ← network-destinations.md
country-deployment/              ← using-the-dashboard.md
.gitbook/assets/                 ← images, country-grid.png, country-codes.txt
.github/
  scripts/update_stats.py        ← daily stats + country flag grid; runs via GitHub Actions
  workflows/update-stats.yml     ← cron 06:00 UTC daily
  tone-guide.md                  ← writing style standard (not published to GitBook)
```

## Key conventions

- **GitBook blocks**: use `{% hint style="info|warning|success" %}`, `{% columns %}` / `{% column %}`, `{% expand %}`, `{% embed url="..." %}` where appropriate
- **Images**: `width="300"` on installation screenshots; full-width for banners
- **Stats block**: between `<!-- stats-start -->` and `<!-- stats-end -->` markers in README.md — updated automatically by GitHub Actions, do not edit manually
- **Buttons**: `<a href="URL" class="button primary">Label</a>`
- **Never push to remote without being asked**
- **No Co-Authored-By trailer on commits**

## Audience tiers (match depth to the page's section)

- **School staff** (Installation, FAQ): plain, task-first, imperative, minimal jargon
- **Government / ministries** (Country Deployment): decision-loop framing, KPIs, ownership, phasing
- **IT / technical teams** (Technical Reference): full mechanism, protocol names, hostnames, ports, API fields
