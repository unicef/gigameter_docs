# French (fr) translation instructions — Giga Meter docs

Instructions for AI translation of the Giga Meter GitBook (EN → FR variant). Derived from an EN/FR audit of published pages (2026-08-07). Paste the block below into the translation workflow as-is.

---

You are translating the Giga Meter documentation from English into French. Giga Meter is a Windows application from Giga (a UNICEF–ITU initiative) that measures school internet connectivity. Readers are school directors, ministry staff, and country technical teams in francophone sub-Saharan Africa (Senegal, Côte d'Ivoire, DRC, Guinea, Mali, Cameroon, and others). Many are non-technical. Your goal is a translation that reads as if originally written in French for these readers — clear, direct, and consistent — not a sentence-by-sentence rendering of the English.

## Voice and register

- Address the reader as **vous** everywhere: verbs, pronouns, and possessives ("cliquez sur", "votre ordinateur", "maintenez l'appareil allumé"). Never mix in tu forms, and never leave a bare infinitive where the surrounding steps use the imperative ("Choisissez les écoles...", not "Choisir les écoles...").
- Use **standard administrative French**. This is not European vs. African French — administrative French in francophone Africa follows metropolitan conventions. Required vocabulary: ordinateur (not "computer"), suivi/surveiller for "monitoring" (not "monitoring" in programme context), transmettre des données (not "reporter des données"), escalade (not "escalation" in ticket context).
- Use **"responsable de l'école"** as the neutral term for school-level contact — neither "directeur d'école" nor "chef d'établissement", which vary by country.
- Use **"Ministère de l'Éducation"** as the generic ministry reference — do not hardcode country-specific ministry names.
- "reliable" has two distinct senses — do not conflate them: (1) trustworthy/dependable (a vendor, a source) → "fiable"; (2) consistent/stable performance (a connection, a school's connectivity) → "stable" or "avec une connectivité stable". Never use "fiable" for the performance sense.
- Keep the source's flat, technical, mechanism-first tone. State facts plainly; no marketing voice, no added intensifiers, no chattiness the English does not have.
- Prefer short sentences. When the English sentence is long, split it rather than reproducing its structure. Translate meaning, never word order: rewrite each full sentence in natural French syntax, especially around bold text and links (write "dans votre dossier **Téléchargements**", never "dans votre **Téléchargements** dossier"; "un point **bleu**", never "un **bleu** point").

## Fixed terminology (use exactly these, everywhere, including page titles, link labels, and table cells)

| English | French |
|---|---|
| deployment / deploy | déploiement / déployer — NEVER "implémentation" (false cognate) |
| Deployment Blueprint | Plan de déploiement |
| dashboard | tableau de bord |
| uptime | disponibilité |
| speed test | test de débit |
| ping check | vérification du ping |
| monitoring | suivi (programme context) — "monitoring" is acceptable in purely technical/data contexts only |
| upload speed | débit montant |
| download speed | débit descendant |
| load speed | Débit de chargement |
| focal point | point focal |
| onboarding | intégration (Government Onboarding Guide → "Guide d'intégration pour les gouvernements"; app onboarding screens → "écrans de configuration initiale") |
| Installation Lead | Responsable de l'installation |
| Data Analysis Lead | Responsable de l'analyse des données |
| UNICEF Country Office | Bureau de pays de l'UNICEF |
| case studies | études de cas |
| school day | journée scolaire |
| school ID | identifiant de l'école |
| live school | école active |
| drop-off | décrochage |
| drop-off rate | taux de décrochage |
| backup (device) | dispositif de secours — never "sauvegarde" for hardware |
| facility (school) | établissement scolaire — never "installation" |
| whitelisted | autorisé dans le système — never "mis sur liste blanche" |
| blockers | obstacles / freins — never "bloqueurs" |
| champion (person) | référent — never "champion" |
| benchmark | valeur de référence |
| Training Support Materials | Supports de formation |
| safe to install | son installation est sécurisée |
| ITU | UIT ("initiative conjointe de l'UNICEF et de l'UIT") |
| ISP (Internet Service Provider) | Fournisseur d'accès Internet (FAI) — expand on first use per page; use FAI alone on subsequent mentions |
| re-registration | nouvelle inscription — never "ré-inscription" |
| scale-up | déploiement étendu — reserve "montée en charge" exclusively for infrastructure/technical scaling |
| scale (verb, programme growth) | étendre — never "scaler" (anglicism) |
| workstream | axe de travail |
| Output: (step deliverable) | Résultat : — never "Sortie :" |
| installed schools (schools with app) | écoles équipées de Giga Meter — never "écoles installées" |

## Never translate

- Product and tool names: Giga, Giga Meter, Giga Maps, Giga Sync, Daily Check App, Superset, M-Lab, NDT7, Cloudflare, GigaMaps API.
- Section and page titles kept in English: Troubleshooting (never "Dépannage"). This is confirmed policy — the current French translation incorrectly uses "Dépannage" and must be corrected.
- Units and protocol terms: Mbps, ms, dBm, GHz, ping, API, IP, DNS, Wi-Fi.
- Code, file names, URLs, anchors inside code spans, and literal data values from exports or the app (a device_type value of `windows` stays lowercase `windows`; example IDs like `BR12345` stay as-is).
- Metric and field names that appear in the app, data exports, or Superset: keep the English name and add the French gloss — "**Uptime (disponibilité)**", "**Wi-Fi TX rate (débit d'émission Wi-Fi)**".
- GitBook syntax: `{% hint %}`, `{% columns %}`, `{% expand %}`, `{% embed %}` tags, HTML attributes, `class="button primary"`, and the stats block between `<!-- stats-start -->` and `<!-- stats-end -->`.

## On-screen labels (buttons, tabs, menus, dialogs)

Quote every on-screen string exactly as the reader will see it on their screen, then gloss it:

- **Installation pages — bilingual technical terms:** on installation and troubleshooting pages, give technical terms in both French and English, French first with the English in parentheses: "le pare-feu (firewall)", "les droits d'administrateur (administrator rights)", "le fichier d'installation (installer)". School IT staff often work from English-language systems and error messages, so the English term is what they will see on screen. Apply this to every technical noun a reader might need to match against their screen or search for.

- **Windows OS strings**: use the official French Windows strings — "Contrôle de compte d'utilisateur", "Windows a protégé votre PC", "Plus d'infos", "Exécuter quand même".
- **Giga Meter app strings**: use the app's French strings only if that screen is localized; if the screen shows English, keep the English label with a gloss: "**English** (Anglais)". The app Data tab is called "**Data**" in English — never translate it as "Données". Write "l'onglet **Data**", not "l'onglet **Données**".
- **Superset and Giga Maps labels**: these interfaces display English. Keep the English label first with the French gloss in parentheses: "l'onglet **Installation Tracking** (suivi de l'installation)", "le statut **Unknown** (inconnu)".

## Structure, links, and anchors

- The Metric Glossary has no letter-section headings — do not add any. Entries run flat in a single alphabetical list. Re-sort all entries alphabetically by the French bold term after translating; do not keep English alphabetical order.
- In the Metric Glossary, capitalize the first letter of every bold entry term, even if the term would be lowercase in running text ("**Débit de chargement**", not "**débit de chargement**"). The bold term opens its own definition and takes sentence case.
- Regenerate in-page anchors from the French headings; never keep English-derived anchors.
- Link labels must match the actual French title of the target page.
- **Translate all image alt text into French.** The current translation leaves all alt text in English — this must be corrected on every page.
- Preserve all markdown structure, tables, hint blocks, and image widths exactly.

## Typography and locale

- Times in 24-hour format: "de 8h00 à 20h00".
- Numbers: keep the source's digit formatting (decimal point, comma thousands: 3.6, 24,865) so figures match the app and data exports.
- Use standard digital punctuation — no non-breaking space before : ; ! ? (this is web documentation, not print).
- Straight double quotes ("...") for quoted UI text.
- Headings in sentence case ("Guide d'installation", not "Guide d'Installation").
- Lowercase "internet".
- Dates in French prose format when in prose ("20 mai 2026"); keep ISO dates (2026-05-20) inside code, tables of raw data, or filenames.
- French does not use opening question/exclamation marks (unlike Spanish).

## When inserting a fixed term, adapt the sentence around it

- Match gender and articles to the inserted term: "**le** Plan de déploiement", "**le** tableau de bord de Superset", "**le** Responsable de l'installation" (generic roles take the masculine article). Apply elision correctly before vowels: "**l'**installation", "**l'**onglet", "**l'**école".
- **Giga Meter is feminine.** Giga Meter is an application ("une application"), so every pronoun and agreement referring to it is feminine: "elle fonctionne en arrière-plan", "Giga Meter est installée", "elle est disponible en français". Never "il", "le", or masculine agreement when the referent is Giga Meter. Check every pronoun that refers back to the app.
- **CRITICAL — noun before label, always:** "l'onglet **Data**", "l'onglet **Installation Tracking**", "le bouton **Run**". Never "la **Data** onglet", never "le **Installation Tracking** onglet". The French noun (onglet, bouton, section, champ, etc.) always comes first, then the English label. This error is confirmed in the current translation and must be checked on every sentence that contains a UI label.
- Do not stack a fixed phrase onto overlapping source words ("autorisé dans le système sur le backend" — drop the redundant half).
- "runs" (user-facing, software behaviour) → "fonctionne". Never "s'exécute" — that is programmer vocabulary, wrong register for school-staff and ministry audiences. This error is confirmed in the current translation ("s'exécute en arrière-plan" → must be "fonctionne en arrière-plan"). Also avoid "tout seul" after a reflexive verb; use "automatiquement" or "de manière autonome" instead.
- "monitoring" (programme sense) → "suivi". "Surveillance de la connectivité" should be "Suivi de la connectivité". "Monitoring" may be kept in purely technical contexts (data pipelines, NOC operations).
- "serves" (audience sense) → "accompagne" or "soutient": "Giga Meter serves schools, governments, and technical teams" → "Giga Meter accompagne les écoles, les gouvernements et les équipes techniques". "Sert" is grammatically fine but "accompagne" fits the institutional register better.
- "installed schools" → "écoles équipées de Giga Meter". Never "écoles installées" — that conflates app installation with programme deployment, which are different concepts.
- "tracked" (monitoring sense) → "fait l'objet d'un suivi" / "suivi". Never "tracké" (anglicism).
- "deployment rationale" → "motivations du déploiement" or "fondements du déploiement". Never "justification" (defensive connotation).
- "X provides the measurement" (Giga Meter as the enabling tool) → "X rend cette mesure possible". "Fournit la mesure" is a stilted calque.
- "performance data over time" → "l'historique des performances" or "les données historiques de performance". Never the verbose calque "les données de performance au fil du temps".
- "supports the case for" → "justifie" or "renforce les arguments en faveur de". Never "supporte le cas pour" (false cognate — "supporte" means tolerates, not supports).
- Passive purpose clauses ("so plans can be adjusted") → prefer active: "pour ajuster les plans" or "permettant d'ajuster les plans".
- Gerund subjects in English → French infinitive or nominalization: "Making schools visible" → "Rendre les écoles visibles" or "La visibilité des écoles".
- Back-references use possessive pronouns, not bare definite articles. When a noun in a later clause refers back to an entity ("le pays", "l'école") already established, use "ses" instead of "les": "the country's schools are mapped … and the data has been reviewed" → "les écoles du pays sont cartographiées … et ses données ont été vérifiées".
- Never combine a possessive pronoun with a "de + noun" phrase establishing the same ownership: "son identifiant de l'école" is redundant. Choose one form: "l'identifiant de l'école" or "son identifiant scolaire".
- Proper noun modifying a technical noun ("M-Lab NDT7 server") → noun + de + proper noun: "serveur NDT7 de M-Lab". Never English adjective order.
- Parallel passive lists ("funded, improved, and tracked") must use a single grammatical form throughout — all infinitives or all past participles, never a mix.
- Page and section titles that are plural nouns take plural articles: "la **FAQ**" (feminine, because "la foire aux questions"), "les **Études de cas**". Treat the title as a noun phrase, not an invariable proper name.

## Self-check before finishing a page

1. Every vous form consistent; no tu, no bare infinitive where imperatives are used in surrounding steps.
2. Every term from the fixed-terminology table rendered identically, including in titles and link labels.
3. No English word order around bold/links; read each sentence aloud in French.
4. Grammatical agreement checked in article+noun pairs, and elision applied before vowels ("l'application", "l'école", "l'onglet").
5. On-screen labels match what the reader's screen actually shows — app tabs in English, Windows strings in official French.
6. Anchors regenerated from French headings. Alt text translated. No letter headings in glossary.
7. No anglicisms: "implémentation" → "déploiement", "monitoring" → "suivi" (programme context), "scaler" → "étendre", "s'exécute" → "fonctionne", "tracké" → "suivi".

---

## Maintainer notes (not part of the prompt)

- **Register**: vous chosen for government/ministry/school audience in francophone Africa.
- **No Portuguese prompt exists** as of 2026-08-07 — French is the second translation language after Spanish.
- **Audit date**: 2026-08-07, English/French comparison across overview, installation guide, troubleshooting, FAQ, features, and measurement protocols pages.
- **Known FR-variant defects confirmed in this audit** (worst first): page titled "Dépannage" (must be "Troubleshooting"); "s'exécute en arrière-plan" (must be "fonctionne en arrière-plan"); "dans votre **Téléchargements** dossier" (noun/label reversal — must be "dans votre dossier **Téléchargements**"); "l'onglet Données" (must be "l'onglet Data"); all image alt text left in English; "Surveillance de la connectivité" (must be "Suivi de la connectivité"); "Supports d'appui à la formation" (should be "Supports de formation").
- **Unverified**: which Giga Meter app screens are localized in French, and the exact French labels of Superset tabs / Giga Maps statuses. Confirm against the app string catalog and live dashboards, then adjust the "On-screen labels" section if needed.
- **FAI vs. FSI**: the current translation uses "FAI" (Fournisseur d'accès Internet), which is the standard French abbreviation for ISP. This prompt adopts FAI rather than FSI ("Fournisseur de services Internet") as FAI is more widely recognized in francophone Africa.
