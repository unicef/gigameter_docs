# Technical Documentation Tone Guide

*A reusable style standard for technical/reference documentation, distilled from the Giga Meter Knowledge Base work (June-July 2026). Written to be reused on future technical documents.*

*Last updated: 2026-07-17*

---

## 1. Purpose and provenance

This guide captures the writing voice we settled on for the **Giga Meter Knowledge Base** (a customer- and government-facing docs site on GitBook) and generalises it so it can be applied to any technical or reference document.

The one-line version: **write like an engineer documenting a system, not like marketing describing a product.**

### Where the tone comes from (cite these)

The voice is deliberately modelled on established network-measurement and infrastructure documentation, not on generic "content writing." When in doubt, go read these and match their register:

- **perfSONAR documentation** - `https://docs.perfsonar.net/` . The reference standard for network-performance measurement docs. Flat, declarative, mechanism-first. Notice how it explains *what a component does and why*, states constraints plainly, and never sells.
- **Kentik "Kentipedia"** - `https://www.kentik.com/kentipedia/` . Network-technical explainers that stay concrete and instructional even when introducing a concept to a newcomer. Educational without being chatty.

These two are the tone anchors. If a draft sentence would look out of place in perfSONAR's docs or a Kentipedia article, it's probably off-voice.

### What replaced what

The KB originally read in a "claudey"/marketing voice - rule-of-three pitch fragments, inserted aphorisms, chipper filler, confident-sounding generalities. The rewrite (CRs #33/#35/#36, then targeted follow-ups through #40) stripped that out in favour of the flat technical register described below.

Pre-rewrite exports of two pages (`overview.md`, `features.md`, saved in `C:\Users\jardi\Downloads\`) are preserved as the "before" corpus; all verbatim before/after pairs in section 7 are quoted from them against the current live KB.

---

## 2. Core principles

1. **Flat and declarative.** State what is true. Let the facts carry the weight; don't add emphasis the facts don't earn.
2. **Mechanism-first.** Explain *how* something works and *why* it behaves that way. A reader of technical docs wants the model in their head, not a benefit.
3. **Precise over impressive.** Prefer the exact, hedged, correct statement to the clean, sweeping one. "Up to 4 per day" beats "frequent." "May test against different servers on different runs" beats "always uses the best server."
4. **Decision-oriented.** For anything operational, tie it to a decision: what triggers a review, who acts, what happens. This is the single most repeated structural move in the KB.
5. **No selling.** The document's job is to inform, not to persuade. Value statements are allowed only when they are also factual and restrained (see 3.2).
6. **Grounded claims only.** Tone must never outrun accuracy. A flat, confident sentence that is *wrong* is worse than an obviously hedged one. (See section 6 - this is the hard-won lesson.)

---

## 3. Sentence-level mechanics

### 3.1 Anti-patterns to delete on sight

These are the specific tics the rewrite targeted. Search for them in any draft:

- **Rule-of-three pitch fragments.** "Faster, simpler, and more reliable." Marketing cadence. The test is whether each of the three items is real content or rhythm-filler. A real example from the KB rewrite ("About Giga"): the slogan triple *"connect every school to the internet and every young person to information, opportunity, and choice"* was cut down to "connect every school to the internet" - but *"technologies that help governments plan, deploy, and sustain school connectivity"* **survived**, because plan/deploy/sustain are three distinct, real phases of the work. Cut cadence, keep content.
- **Inserted aphorisms / mission slogans.** "Because every child deserves to be connected." "Data is the new infrastructure." Delete entirely.
- **Chipper filler.** "Great news!" "It's that simple!" "Don't worry -" "The best part?" These add words and subtract credibility.
- **Empty intensifiers.** "Powerful," "seamless," "robust," "cutting-edge," "world-class," "easy." Either prove it with a fact or drop it.
- **Fake quantification.** "~80% of schools," "most governments," "the vast majority" used rhetorically. If it isn't grounded in real data, don't imply a number. (This is a standing rule: never manufacture quantities for rhetorical effect.)
- **Second-person hype.** "You'll love how easy it is to -" Reserve "you" for genuine instructions ("you need," "you can view").

### 3.2 The one permitted value statement

Flat doesn't mean value-free. A restrained "why this matters" line is acceptable **if it is factual and immediately followed by a concrete claim.** The KB does this exactly once on the overview page. This is a real before/after from the rewrite (source: pre-rewrite `overview.md`, "Why use Giga Meter?"):

> **Before [REAL]:** "You can't improve what you can't measure. Giga Meter makes school connectivity visible, measurable, and actionable - so it can be prioritised, funded, and improved for the learners who depend on it."
>
> **After [REAL]:** "Connectivity that is measured can be funded, improved, and tracked over time. Giga Meter provides the measurement."

What changed and why:
- The opening aphorism ("You can't improve what you can't measure") is a borrowed management slogan - deleted.
- "Visible, measurable, and actionable" is a rhythm triple - deleted.
- "For the learners who depend on it" is an emotional-appeal tail - deleted.
- What survives is the same causal chain, stated once, landing on a plain factual sentence ("Giga Meter provides the measurement") instead of an escalation.

**One such line per page, maximum.** If you find two, one is filler.

### 3.3 Voice, tense, hedging

- **Present tense, active voice, concrete subject.** "The app calls `locate.measurementlab.net`..." not "A call is made to..."
- **Hedge precisely, not vaguely.** "May test against different servers on different runs, particularly if M-Lab adds or removes servers" is a *precise* hedge - it says exactly when the variance happens. Avoid vague hedges ("sometimes," "in certain cases") that add uncertainty without adding information.
- **State constraints with their reason.** Pattern: `[constraint], because [mechanism].`
  > **[Real KB text - Measurement Protocols]**
  > "A static IP list is not feasible and is not maintained, because M-Lab's server pool changes regularly."
- **Define by contrast when a term is easily misread.**
  > **[Real KB text - Data Analysis Lead Guide]**
  > "A use case is not a general goal ('understand school connectivity'). It is a specific decision loop: what condition triggers a review, who reviews it, and what action results."

### 3.4 Formatting conventions (house style)

- **No emoji, no emoticons.** Anywhere. (The KB's Giga Maps status table uses coloured-dot glyphs as *data labels* for the actual map colours - that's a legend, not decoration. Don't generalise it into emoji-as-flavour.)
- **No en dashes.** Use a plain hyphen (`-`) for ranges, parentheticals, and joins. This applies even where a typographer would use an en dash.
- **Concision.** Every sentence should lose a word if it can. Prefer the shorter construction that keeps the precision.
- **Code/hostnames in backticks.** `*.measurementlab.net`, `speed.cloudflare.com`, `ServerInfo.Country`.
- **Numbers stay specific.** "Up to 4 per day," "8am-8pm local time," "port 443." Don't round to "several" or "during the day" when you have the real figure.

---

## 4. Structural patterns

These are the repeatable page-level moves the KB uses. Reach for them before inventing a new structure.

### 4.1 The decision-loop template (for operational/deployment content)

Every case study and most operational guidance follows the same skeleton:

```
Context:            the situation / constraint that created the need
Use case:           what the data is actually used for
Decision triggered: the specific condition -> action -> owner
What makes it work: the mechanism that makes the model robust (optional)
```

> **[Real KB text - Case Studies, Brazil]**
> "Decision triggered: Schools below the per-student threshold are flagged for ISP follow-up. ISP fiscal benefit claims are accepted only when validated against live measurement data."

This keeps operational docs from drifting into aspiration. If you can't fill in "decision triggered," the content probably isn't ready to document.

### 4.2 Concrete-example grounding

When stating that context matters, immediately prove it with a concrete, realistic example - and never with a fabricated statistic:

> **[Real KB text - Data Analysis Lead Guide]**
> "Context matters. A 5 Mbps download speed may be poor for a school with 200 students but adequate for a rural primary with 30."

### 4.3 Tables for anything enumerable

Measurement schedules, server tiers, status legends, metric definitions, KPIs - all tables. Prose is for explaining relationships and mechanisms; tables are for lookups. The Measurement Protocols page is almost entirely intro-sentence-then-table.

### 4.4 Callout/hint blocks for out-of-band notes

Version notes, "keep the device on" reminders, and protocol-change notes go in hint blocks (`{% hint style="info" %}` in GitBook), not inline. This keeps the main line of the doc clean and reserves the reader's attention.

### 4.5 Headings are navigation, not slogans

Section headings are literal and scannable: "Speed test," "Measurement schedule," "Connectivity status on Giga Maps." Never a teaser heading ("Measurement, made simple"). A reader scanning the outline should be able to jump straight to what they need.

---

## 5. Audience calibration

The same fact gets pitched at different depth depending on who the page is for. The KB has three implicit audiences; match the register to the page's section:

- **School staff** (Installation, FAQ): plain, task-first, minimal jargon, imperative instructions. "Visit maps.giga.global/map, type your school name in the left-hand panel, and select it."
- **Government / ministries** (Country Deployment): decision-loop framing, KPIs, ownership, rollout phasing. Assumes a planner, not an engineer.
- **IT / technical teams** (Technical Reference): full mechanism, protocol names, hostnames, ports, API fields. Assumes the reader wants to whitelist, integrate, or debug.

Calibrating *down* for school staff is still flat - it's simpler, not chattier. Simplicity and chattiness are different axes; keep the first, never add the second.

---

## 6. Accuracy discipline (tone must not outrun facts)

This is the most important section and the one learned the hard way.

A flat, confident technical voice is *persuasive by construction* - it reads as authoritative. That makes it dangerous when the underlying claim is wrong, because nothing in the prose signals doubt. **The voice raises the bar for factual correctness; it does not lower it.**

### Worked cautionary example (real, this session)

On the "Connectivity status on Giga Maps" table, I added what looked like a perfectly on-voice clarifying sentence:

> **[Real edit, CR #41 - later reverted]**
> "The benchmark is set per country: a school is graded against its own country's connectivity target, not a single global speed."

It has every tonal virtue in this guide: flat, declarative, colon-then-clarification, no filler. It was also **factually wrong** - the Giga Maps benchmark is a *selectable* value that is sometimes a global figure (e.g. 20 Mbps). The existing wording ("meets selected benchmark") was already correct. I archived the change request; nothing shipped.

**The lesson:** when a sentence sounds authoritative, verify it *harder*, not less. Specifically:
- Ground every added claim in a source you can point to (existing KB text, a primary system, the actual product behaviour) - not in what sounds plausible.
- If two places in the docs disagree (as the jitter/packet-loss question still does), that's a blocker to escalate, not a gap to smooth over with confident prose.
- "Reads well" and "is true" are independent checks. Pass both.

### Related standing rules

- **No manufactured quantities** (restated from 3.1) - the flat voice makes a fake "~80%" look like a real measurement.
- **Leave stale-but-harmless hardcoded facts alone if the fix is worse than the rot.** The Introduction's hardcoded counts (39 countries / 20,978 schools / 3,091,134 measurements) are frozen snapshots, but live-binding them wasn't worth the maintenance - a deliberate call, not an oversight. Tone work shouldn't create fragile machinery.

---

## 7. Before / after examples

All pairs below are **real edits** from the KB rewrite unless tagged **[ILLUSTRATION]**. "Before" text is quoted verbatim from the pre-rewrite page exports (`overview.md`, `features.md` - archived copies in `Downloads\`); "after" text is the current live KB.

### 7.1 Feature-card captions (About Giga Meter)

The three benefit cards on the overview page are the clearest side-by-side of the whole rewrite - same layout, same facts, different voice:

| Before [REAL] | After [REAL] |
| --- | --- |
| **Effortless automation** - "The Windows app runs seamlessly with minimal user input and data usage." | **Automated measurement** - "The Windows app runs in the background with minimal user input and low data usage." |
| **Reliable internet monitoring** - "Quickly identify schools that aren't meeting benchmarks." | **Connectivity monitoring** - "Identifies schools that are not meeting connectivity benchmarks." |
| **Data-driven connectivity planning** - "Use performance data to adapt plans and optimize internet quality for your schools." | **Data for planning** - "Performance data over time supports connectivity planning and procurement." |

*What changed:* every card title dropped its adjective ("Effortless" -> "Automated", "Reliable" -> nothing, "Data-driven" -> "Data for"). "Seamlessly" (unverifiable) became "in the background" (a mechanism). "Quickly" (a promise) was cut. The imperative sales-pitch "Use... to optimize... for your schools" became a declarative statement of what the data supports. Titles now name the function, not the feeling.

### 7.2 The "what is it" paragraph (About Giga Meter)

- **Before [REAL]:** "By leveraging data from Giga Meter, governments and school administrators can make informed decisions that enhance school internet services, ultimately improving students' digital learning experiences."
- **After [REAL]:** "The resulting data lets governments and school administrators see where connectivity falls short and decide where to direct investment and support."

*Why:* "leveraging," "informed decisions," "enhance," "ultimately improving... experiences" is four abstractions in a row - none of them says what anyone actually does. The after names the two concrete actions the data enables: see where connectivity falls short, decide where to direct investment.

### 7.3 The "why it matters" line (About Giga Meter)

- **Before [REAL]:** "You can't improve what you can't measure. Giga Meter makes school connectivity visible, measurable, and actionable - so it can be prioritised, funded, and improved for the learners who depend on it."
- **After [REAL]:** "Connectivity that is measured can be funded, improved, and tracked over time. Giga Meter provides the measurement."

*Why:* aphorism cut, rhythm triple cut, emotional tail cut; same causal chain, stated once. (Full dissection in section 3.2.)

### 7.4 Mission framing (About Giga)

- **Before [REAL]:** "Giga is a UNICEF-ITU initiative to connect every school to the internet and every young person to information, opportunity, and choice."
- **After [REAL]:** "Giga is a UNICEF-ITU initiative to connect every school to the internet. It develops and maintains open-source technologies that help governments plan, deploy, and sustain school connectivity."

*Why:* the slogan triple ("information, opportunity, and choice") is gone; the content triple ("plan, deploy, and sustain") stays because each item is a distinct phase of real work. The mission statement now ends where the facts end.

### 7.5 Audience tabs - slogan headers removed (About Giga Meter)

The "What it means for you" tabs kept their structure but lost their bolded mini-slogan headers:

- **Before [REAL - School principals & teachers tab]:** "**Make a stronger case for support** - Real data collected over time lets you advocate for better internet, equipment, or funding. Evidence transforms local concerns into actionable priorities."
- **After [REAL]:** "Measurement data collected over time supports the case for better internet, equipment, or funding."

- **Before [REAL - Learners tab]:** "**No learner left offline** - Ensuring underserved schools are visible means the students who need support most are more likely to get it."
- **After [REAL]:** "Making underserved schools visible increases the likelihood that the students who need support most will receive it."

*Why:* "No learner left offline" is a campaign slogan; "Evidence transforms local concerns into actionable priorities" is an inserted aphorism. Both deleted. The surviving sentences state the same mechanism in one plain clause each. Note the after is not colder in substance - it says the same hopeful thing - it just refuses the poster voice.

### 7.6 Opening a technical page

- **Before [ILLUSTRATION]:** "Giga Meter is a powerful, easy-to-use tool that gives you everything you need to understand your school's connectivity - all in one place."
- **After [REAL - Measurement Protocols]:** "Giga Meter uses two tests to assess internet quality at schools: a speed test and a ping test."

*Why:* the after names the actual mechanism (two tests) in the first sentence. No adjectives, no promise, straight into the model.

### 7.7 Explaining a constraint

- **Before [ILLUSTRATION]:** "Giga Meter is smart about servers - it always connects you to the best available option for lightning-fast results."
- **After [REAL - Measurement Protocols]:** "Because the server is selected at runtime, the same school may test against different servers on different runs, particularly if M-Lab adds, removes, or takes servers offline for maintenance."

*Why:* the after is honest about variance and explains its cause. "Always... best... lightning-fast" is three unverifiable claims in one line.

### 7.8 Operational guidance

- **Before [ILLUSTRATION]:** "Use Giga Meter data to keep an eye on how your schools are doing and make sure everyone stays connected."
- **After [REAL - Case Studies, Brazil]:** "Decision triggered: Schools below the per-student threshold are flagged for ISP follow-up. ISP fiscal benefit claims are accepted only when validated against live measurement data."

*Why:* the after specifies condition, action, and validation rule. The before is a vibe.

### 7.9 A precise numeric reconciliation

- **Before [REAL - pre-rewrite `features.md`]:** "Up to 3 app instances can be registered per school" (and "Up to 3 devices per school" in the comparison table) - while other pages said different numbers.
- **After [REAL - CR #40, applied across all pages]:** "up to 5 per school, one is enough to get started."

*Why:* beyond fixing the figure, the reconciliation picked one phrasing that carries both the ceiling and the practical minimum, and applied it *everywhere*. Cross-page consistency of a spec figure is a tone issue too: a doc set that disagrees with itself reads as unmaintained, no matter how flat the prose. (See also section 6 - the jitter/packet-loss cross-page contradiction is the open case of the same problem.)

### 7.10 What the old docs got right (keep it)

Not everything pre-rewrite was marketing - and it's worth naming what already matched the target voice, because the rewrite *kept* it. From the pre-rewrite `features.md`:

> "Tests run against the nearest available M-Lab server, measuring the connection to the public internet - not local network speed to the router."

> "Geolocation validation: Measurements are automatically flagged if the device is more than 4km from the registered school location, or if GPS accuracy falls below 500m."

Define-by-contrast, exact thresholds, mechanism-first - already on-voice. A tone pass is surgical: it removes the pitch layer and leaves substance untouched. If a rewrite is churning sentences like these, it has overshot.

---

## 8. Quick pre-publish checklist

Run every draft through this:

- [ ] Would this sentence look at home in perfSONAR docs or a Kentipedia article? If not, reflatten it.
- [ ] Any rule-of-three fragments, aphorisms, or chipper filler? Delete.
- [ ] Any adjective doing work a fact should do ("powerful," "seamless," "easy")? Replace with the fact or cut.
- [ ] Any number implied for effect but not grounded in data? Remove.
- [ ] Is every operational claim tied to a decision (trigger -> action -> owner)?
- [ ] Are constraints stated *with their reason*?
- [ ] Is every added factual claim traceable to a real source, not just plausible? Verify the authoritative-sounding ones hardest.
- [ ] Anything enumerable in prose that should be a table?
- [ ] No emoji, no en dashes (plain hyphens only).
- [ ] Does the register match the page's audience (staff / government / technical) without getting chatty?

---

## 9. One-paragraph summary (for pasting into a prompt)

> Write in a flat, technical, mechanism-first register modelled on perfSONAR documentation and Kentik's Kentipedia. State facts plainly and let them carry the weight; explain how things work and why they behave that way. No marketing voice: no rule-of-three pitch fragments, no aphorisms or mission slogans, no chipper filler, no empty intensifiers (powerful/seamless/easy), no quantities that aren't grounded in real data. Tie operational content to decisions (what triggers a review, who acts, what happens). State constraints with their reason. Hedge precisely, not vaguely. Use tables for anything enumerable and callout blocks for out-of-band notes. Match depth to audience (school staff / government / technical) without getting chatty. Above all, never let the confident voice outrun the facts: verify authoritative-sounding claims harder, and ground every added statement in a real source. No emoji, no en dashes.
