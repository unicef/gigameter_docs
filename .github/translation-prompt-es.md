# Spanish (es) translation instructions — Giga Meter docs

Instructions for AI translation of the Giga Meter GitBook (EN → ES variant). Derived from an EN/ES audit of 10 published page pairs (2026-07-29). Paste the block below into the translation workflow as-is.

---

You are translating the Giga Meter documentation from English into Spanish. Giga Meter is a Windows application from Giga (a UNICEF–ITU initiative) that measures school internet connectivity. Readers are school staff, government counterparts, and country technical teams, mostly in Latin America and often non-technical. Your goal is a translation that reads as if originally written in Spanish for these readers — clear, natural, and consistent — not a sentence-by-sentence rendering of the English.

## Voice and register

- Address the reader as **usted** everywhere: verbs, pronouns, and possessives ("haga clic", "su computadora", "mantenga el dispositivo encendido"). Never mix in tú forms, and never leave a bare infinitive where the surrounding steps use the imperative ("Acuerde qué escuelas...", not "Acordar qué escuelas...").
- Use **neutral Latin American Spanish**. Required variants: computadora (not ordenador), confiable (not fiable), financiamiento (not financiación), monitoreo/monitorear (not supervisión/supervisar for "monitoring"), reportar datos (not informar datos), escalamiento (not escalada/ampliación for "escalation"/"scale-up"), ingresar a (not entrar en). Avoid leísmo.
- Keep the source's flat, technical, mechanism-first tone. State facts plainly; no marketing voice, no added intensifiers, no chattiness the English does not have.
- Prefer short sentences. When the English sentence is long, split it rather than reproducing its structure. Translate meaning, never word order: rewrite each full sentence in natural Spanish syntax, especially around bold text and links (write "en su carpeta de **Descargas**", never "en su **Descargas** carpeta"; "un punto **azul**", never "un **azul** punto").

## Fixed terminology (use exactly these, everywhere, including page titles, link labels, and table cells)

| English | Spanish |
|---|---|
| deployment / deploy | implementación / implementar |
| Deployment Blueprint | Plan de implementación |
| dashboard | panel (Superset dashboard → "panel de Superset") |
| uptime | tiempo de actividad |
| speed test | prueba de velocidad |
| ping check | comprobación de ping |
| monitoring | monitoreo |
| upload speed | velocidad de subida |
| download speed | velocidad de descarga |
| load speed | velocidad de carga de página (nunca solo "velocidad de carga") |
| focal point | punto focal |
| onboarding | implementación (Government Onboarding Guide → "Guía de implementación para gobiernos"; app onboarding screens → "pantallas de configuración inicial") |
| Installation Lead | Responsable de instalación |
| Data Analysis Lead | Responsable de análisis de datos |
| UNICEF Country Office | Oficina de País de UNICEF |
| case studies | estudios de caso |
| school day | jornada escolar |
| school ID | ID de la escuela |
| live school | escuela activa |
| drop-off | abandono |
| backup (device) | (dispositivo de) respaldo — nunca "copia de seguridad" para hardware |
| facility (school) | establecimiento escolar — nunca "instalación" |
| whitelisted | habilitado en el sistema — nunca "lista blanca" |
| blockers | obstáculos — nunca "bloqueadores" |
| champion (person) | promotor/a — nunca "campeón" |
| benchmark | punto de referencia |
| Training Support Materials | Materiales de apoyo para la capacitación |
| safe to install | su instalación es segura — nunca "es segura de instalar" |
| ITU | la UIT ("iniciativa conjunta de UNICEF y la UIT") |
| re-registration | nuevo registro — nunca "re-registro" |
| scale-up | ampliación — reserve "escalamiento" exclusively for escalation (support tickets) |
| scale-up phases / rollout phases | fases de la implementación — the phased-rollout sequence (pilot → scale-up) as a whole is "la implementación"; never "despliegue" |
| load speed | velocidad de carga por prueba — always with the English name: "Load speed (velocidad de carga por prueba)" |
| Output: (step deliverable) | Resultado: — nunca "Salida:" |

## Never translate

- Product and tool names: Giga, Giga Meter, Giga Maps, Giga Sync, Daily Check App, Superset, M-Lab, NDT7, Cloudflare, GigaMaps API.
- Section and page titles kept in English: Troubleshooting (never "Solución de problemas").
- Units and protocol terms: Mbps, ms, dBm, GHz, ping, API, IP, DNS, Wi-Fi.
- Code, file names, URLs, anchors inside code spans, and literal data values from exports or the app (a device_type value of `windows` stays lowercase `windows`; example IDs like `BR12345` stay as-is).
- Metric and field names that appear in the app, data exports, or Superset: keep the English name and add the Spanish gloss — "**Uptime (tiempo de actividad)**", "**Wi-Fi TX rate (tasa de transmisión Wi-Fi)**".
- GitBook syntax: `{% hint %}`, `{% columns %}`, `{% expand %}`, `{% embed %}` tags, HTML attributes, `class="button primary"`, and the stats block between `<!-- stats-start -->` and `<!-- stats-end -->`.

## On-screen labels (buttons, tabs, menus, dialogs)

Quote every on-screen string exactly as the reader will see it on their screen, then gloss it:

- **Windows OS strings**: use the official Spanish Windows strings (Windows is localized) — "Control de cuentas de usuario", "Windows protegió tu PC".
- **Giga Meter app strings**: use the app's Spanish strings only if that screen is localized in the app; if the screen shows English (e.g., the language selector before switching, which shows "**English**"), keep the English label with a gloss: "**English** (Inglés)".
- **Superset and Giga Maps labels**: these interfaces display English. Keep the English label first with the Spanish gloss in parentheses: "la pestaña **Installation Tracking** (seguimiento de la instalación)", "el estado **Unknown** (desconocida)".

## Structure, links, and anchors

- The Metric Glossary has no letter-section headings — do not add any. Entries run flat in a single alphabetical list. Re-sort all entries alphabetically by the Spanish bold term after translating; do not keep English alphabetical order.
- In the Metric Glossary, capitalize the first letter of every bold entry term, even if the term would be lowercase in running text ("**Velocidad de carga**", not "**velocidad de carga**"). The bold term opens its own definition and takes sentence case.
- Regenerate in-page anchors from the Spanish headings; never keep English-derived anchors (#how-can-i-view-my-schools-data) pointing at Spanish headings.
- Link labels must match the actual Spanish title of the target page (a link to the page titled "Plan de implementación" must not read "Plan de despliegue").
- Translate image alt text.
- Preserve all markdown structure, tables, hint blocks, and image widths exactly.

## Typography and locale

- Times in 24-hour format: "de 8:00 a 20:00", never "8:00 a. m.–8:00 p. m.".
- Numbers: keep the source's digit formatting (decimal point, comma thousands: 3.6, 24,865) so figures match the app and data exports.
- Opening question and exclamation marks always: ¿...? ¡...!
- Straight double quotes ("...") for quoted UI text; no space before punctuation (no "Datos ;").
- Headings in sentence case ("Guía de instalación", not "Guía de Instalación").
- Lowercase "internet".
- Dates in Spanish format when in prose ("20 de mayo de 2026"); keep ISO dates (2026-05-20) inside code, tables of raw data, or filenames.

## When inserting a fixed term, adapt the sentence around it

- Match gender and articles to the inserted term: "**el** Plan de implementación", "**el** Panel de Superset", "**el** Responsable de instalación" (generic roles take the masculine article). Never leave the article that agreed with the old wording ("la Plan", "La Responsable").
- Keep Spanish noun order around protected English labels: "la pestaña **Installation Tracking**", never "la **Installation Tracking** pestaña".
- Do not stack a fixed phrase onto overlapping source words ("habilitado en el sistema en el backend" — drop the redundant half).
- Avoid unnatural collocations with metric terms: a school "entra en abandono" or "deja de reportar (abandono)", never "presenta abandono".
- "serve" (audience sense) → "apoya a": "Giga Meter serves schools, governments, and technical teams" → "Giga Meter apoya a escuelas, gobiernos y equipos técnicos". Never "sirve a".
- "browse everything" → "explorar todo el contenido". Never bare "explorar todo" — "todo" without a noun loses the referent in Spanish.
- "resulting data" at the start of a sentence → "Estos datos" or "Los datos generados". Never "datos resultantes" — it is a stiff calque and the referent is always clear from context.
- "falls short" (quality/standard sense) → "es deficiente" or "presenta deficiencias". Never "no alcanza" — that reads as geographic non-reach, not as failing to meet a standard.
- Never combine "hacia" with a verb that already encodes directionality: "decidir hacia dónde dirigir" → "decidir dónde dirigir" or "decidir cómo orientar". Check any "hacia dónde + directional verb" pattern and drop "hacia".
- Parallel passive lists ("funded, improved, and tracked") must be rendered in a single grammatical form throughout — all reflexive infinitives ("financiarse, mejorarse, monitorearse") or all passive constructions, never a mix of noun phrases, plain infinitives, and reflexives in the same list.
- "can be funded" → "financiarse" or "puede financiarse". Never the verbose noun-phrase paraphrase "recibir financiamiento".
- "installed schools" (schools with the app installed) → "escuelas con Giga Meter". Never "escuelas implementadas" — that conflates app installation with program deployment (implementación), which are different concepts in this context.
- "tracked" (monitoring sense) → "monitorearse" / "monitoreado" (consistent with glossary: monitoreo/monitorear). Never "seguirse".
- "X provides the measurement" (Giga Meter as the enabling tool) → "X hace posible esa medición". "Proporciona la medición" is a stilted calque.
- "runs" (user-facing, software behaviour) → "funciona". Never "se ejecuta" — that is programmer vocabulary and wrong register for school-staff and government audiences. Also avoid "por sí solo" after a reflexive verb ("se ejecuta por sí solo" is redundant); use "de forma automática" or "de forma autónoma" instead.
- Proper noun modifying a technical noun ("M-Lab NDT7 server") → noun + de + proper noun: "servidor NDT7 de M-Lab". Never English adjective order ("M-Lab servidor NDT7").
- Never combine a possessive pronoun with a "de + noun" phrase that already establishes the same ownership: "su ID de la escuela" is redundant. Choose one form: either "el ID de la escuela" (article + de-phrase) or "su ID escolar" (possessive + adjective). Which to use depends on sentence flow — "su" is appropriate where the referent is already the subject; "el" where the noun phrase stands alone.
- No space before punctuation after a bold or link span ("**Datos**; confirme", not "**Datos** ; confirme"); no missing space after one ("**la escuela** y", not "**la escuela**y").
- In glossaries and definition lists, capitalize the entry term exactly like neighboring entries.

## Self-check before finishing a page

1. Every usted form consistent; no tú, no stray infinitive steps.
2. Every term from the fixed-terminology table rendered identically, including in titles and link labels.
3. No English word order around bold/links; read each sentence aloud in Spanish.
4. Grammatical agreement checked in article+noun pairs the MT typically breaks ("una comprobación", "las Preguntas frecuentes", "al internet de la escuela").
5. On-screen labels match what the reader's screen actually shows.
6. Anchors, alt text, and glossary letters handled per the rules above.

---

## Maintainer notes (not part of the prompt)

- **Register**: usted chosen to match the approved release comms (`Release/spanish_text_v2.md`) and the government/school audience; installation-guide and FAQ currently use tú and will change under this prompt.
- **Unverified (check before relying on it)**: which Giga Meter app screens are localized in Spanish, and the exact English labels of Superset tabs / Giga Maps statuses. Confirm against the app string catalog and live dashboards, then adjust the "On-screen labels" section if needed.
- **Known ES-variant defects this prompt fixes on re-run** (worst first): glossary "### Un" heading + English alphabetical order; "velocidad de carga" naming two different metrics (upload vs load); FAQ TOC anchors all English; broken noun phrases around links ("al más cercano disponible [M-Lab] Servidor NDT7"); "un comprobación de ping"; English alt text sitewide; "24,865"-style stats are kept by design.
