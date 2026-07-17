# Data Analysis Lead Guide

This guide is for the government official responsible for ensuring Giga Meter data is used, from defining what to measure through to embedding analysis in ongoing decision-making. Work through these steps in parallel with the installation workstream.

← [Government Onboarding Guide](government-onboarding-overview.md)

***

### Step 1 - Define the use case

Before onboarding any user to the dashboard, define what the government will use Giga Meter data for. This shapes which KPIs to track and which decisions the data will inform.

A use case is not a general goal ("understand school connectivity"). It is a specific decision loop: what condition triggers a review, who reviews it, and what action results.

{% hint style="warning" %}
Without a defined use case, dashboard users tend to look at the data without knowing what to do with it. The use case definition is the foundation of the data analysis workstream.
{% endhint %}

**A use case answers three questions:**

1. **What decision will this data inform?** e.g. which schools to prioritise for ISP upgrades; whether a provider is meeting contract terms; whether a national connectivity target is on track
2. **Who makes that decision?** e.g. the MoE IT unit, the planning department, the minister
3. **How often is that decision made?** e.g. monthly for operational reviews, annually for budget planning

**Examples from Giga deployments:**

| Country                     | Use case                                                                                                                                                                                                                                                                                               | Decision triggered                                                                                                                       |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| [Brazil](case-studies.md)   | Enforce 1 Mbps per enrolled student in longest shift (ENEC policy)                                                                                                                                                                                                                                     | Schools below threshold flagged for ISP follow-up; ISP fiscal benefit claims validated against measured data                             |
| Moldova                     | Monitor connectivity quality in a decentralised system where all schools are connected but quality is unmonitored and no benchmarks exist; verify that schools meet connectivity prerequisites for mandatory platforms (Electronic Catalog/SICE requires high-speed and secure network infrastructure) | Schools not meeting quality thresholds flagged for ISP contract review; data supports planning for Model School infrastructure standards |
| [Mongolia](case-studies.md) | Triangulate LAN performance to diagnose ISP vs. infrastructure issues; inform decentralised ISP contracting                                                                                                                                                                                            | Schools with poor end-device performance despite healthy routers escalated to ISP-side investigation                                     |
| [Fiji](case-studies.md)     | Identify which schools have stable enough connectivity for live broadcast STEM lessons                                                                                                                                                                                                                 | Only schools confirmed reliable over monitoring period enrolled in the live lesson programme                                             |
| [Botswana](case-studies.md) | Track compliance against 100 Mbps national mandate (Village Connectivity Project)                                                                                                                                                                                                                      | Schools below mandate identified for ISP renegotiation or infrastructure upgrade                                                         |
| Malawi                      | Establish independent baseline of student-experienced speeds vs. ISP-reported speeds                                                                                                                                                                                                                   | Evidence base for government accountability proceedings with ISPs                                                                        |
| General                     | Deployment monitoring                                                                                                                                                                                                                                                                                  | Schools not reporting within 7 days get a follow-up call from the regional coordinator                                                   |

→ [Case Studies - full country deep dives](case-studies.md)

**Writing your use case**

Aim for one paragraph. It should answer: what is being monitored, what counts as a problem, and who acts on it. The examples below show two types:

> _Policy enforcement:_ "We are using Giga Meter to monitor whether schools meet the national benchmark of 1 Mbps per enrolled student. Schools below threshold for two consecutive weeks are reported to the ISP coordinator. Compliance is reviewed monthly by the MoE IT department."

> _Programme readiness:_ "We are using Giga Meter to identify which schools have reliable enough connectivity to participate in live broadcast STEM lessons. Schools with confirmed stable download speeds over the previous 30 days are cleared for enrolment. The list is updated monthly by the MoE Digital Education team."

**Connecting use case to KPIs**

Once the use case is clear, define the KPIs that operationalise it. See Step 5.

| Use case type               | Typical KPIs                                                                                   |
| --------------------------- | ---------------------------------------------------------------------------------------------- |
| Policy enforcement          | % schools meeting national speed benchmark; # schools below benchmark for 30+ consecutive days |
| ISP contract compliance     | % schools receiving ≥ 80% of contracted speed; # days below SLA threshold per school           |
| Digital education readiness | % schools meeting meaningful connectivity threshold; # schools cleared for programme enrolment |
| Deployment monitoring       | % installed schools reporting in last 7 days; # schools with 28+ day data gap                  |
| Baseline and trend analysis | Average download speed per district per quarter; YoY change in median latency                  |

**Output:** A short document specifying which decisions Giga Meter data will inform. Share with the Giga team before the first dashboard onboarding session.

{% hint style="info" %}
**Use case definition**\
What we are monitoring:\
Threshold or condition that signals a problem:\
Who is responsible for acting on it:\
What action is taken:\
How often is it reviewed:
{% endhint %}

***

### Step 2 - Identify data users and assign access roles

Identify who in the ministry, and beyond, needs Giga Meter data and at what level. Not everyone needs the same access. School-level focal points may need to see their own school on Giga Maps; regional coordinators may need a filtered view of their region; ministry analysts may need national export access.

**Common access patterns:**

| Role                             | Typical channel | Access scope         |
| -------------------------------- | --------------- | -------------------- |
| Planning director / minister     | Dashboard       | National view        |
| MoE IT coordinator               | Dashboard + API | All schools          |
| Regional coordinator             | Dashboard       | Regional filter only |
| School focal point               | Giga Maps       | Own school only      |
| Technical partner / data analyst | API             | Full export          |

**Output:** Share the confirmed list of users and their required access levels with the Giga team. Dashboard and API accounts are role-based and must be provisioned; users cannot self-register.

***

### Step 3 - Onboard data users to their access channels

Giga Meter data is accessible through two channels. Which channel a user needs depends on how they work with data.

| Channel                                                | Best for                                                                                                               | Access                                |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| [**Superset Dashboard**](https://superset.giga.global) | Policy teams, ministry staff, country coordinators who need charts and tables without writing code                     | Login credentials provisioned by Giga |
| [**API**](https://maps.giga.global/docs/api/1)         | Technical teams, data analysts, partners who want to integrate Giga data into their own systems or run custom analyses | API key provisioned by Giga           |
| **Giga Maps**                                          | Schools, regional focal points, and the public viewing a school's connectivity dot                                     | Public, no credentials needed         |

Both channels access the same underlying data. The difference is presentation and flexibility.

[**Superset Dashboard**](https://superset.giga.global)

The dashboard provides seven pre-built screens covering school-level summaries, speed and latency trends, district breakdowns, per-measurement data tables, app version tracking, and installation health.

_Getting access:_ Users create their own account at [superset.giga.global](https://superset.giga.global), then share their registered email with the Giga team, who assign the appropriate country-level role. Without role assignment, users can log in but will not see any data.

_What users can do:_ filter by school, district, date range, and education level; export any table to CSV; view time series, box plots, and distribution charts; share direct links to specific dashboard views.

_What users cannot do:_ edit the dashboard or charts (read-only); access data from other countries.

[**API**](https://maps.giga.global/docs/api/1)

The Giga Maps API provides programmatic access to school connectivity data, for teams that want to pull data into their own tools, build automated reports, or integrate Giga data into government systems.

_Getting access:_ Contact the Giga team through your UNICEF country focal point to request an API key and documentation.

_What the API provides:_ school-level measurements (download speed, upload speed, latency, uptime); school metadata (location, education level, government ID); time-series data queryable by school, district, and date range; data licensed under CC BY 4.0.

**Run onboarding before the first data review.** Do not let the first time users see the data be in a meeting where they are expected to interpret it.

**Output:** Every identified user has logged in and can independently pull the data they need for their role.

{% hint style="info" %}
**Onboarding milestone**\
Onboarding session format: \[e.g. live walkthrough, recorded video, written guide]\
Date completed:\
Users onboarded: \[N]\
Users pending: \[N - names and reason for delay]
{% endhint %}

**Dashboard screens.** The dashboard has seven pre-built screens covering school summaries, speed and latency trends, district breakdowns, per-measurement tables, app-version tracking, and installation health. For a screen-by-screen reference of what each column and chart means, see [Using the Dashboard](../../country-deployment/using-the-dashboard.md).

***

### Step 4 - Establish metric literacy

Giga Meter reports several technical metrics. Before users draw conclusions from the data, circulate a simple reference explaining what each metric means and what a good or problematic value looks like in the country's context.

Context matters. A 5 Mbps download speed may be poor for a school with 200 students but adequate for a rural primary with 30. Setting country-specific or school-type-specific thresholds makes the data more actionable than global benchmarks alone.

**Key metrics:**

| Metric                    | What it measures                                                         | As a rough guide                                                       |
| ------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **Download speed** (Mbps) | Rate at which the school receives data from the internet                 | 1 Mbps per participant for audio calls; 5 Mbps+ for HD video per class |
| **Upload speed** (Mbps)   | Rate at which the school sends data, the outgoing side of a video call   | Usually lower than download; asymmetric links are normal               |
| **Latency** (ms)          | Delay between a request and the first response                           | Under 50 ms feels instant; over 200 ms causes noticeable lag           |
| **Uptime** (%)            | Share of school hours (8am-8pm) where the connection is confirmed active | 99% = unreachable at most \~3.6 hours of school time/month             |
| **Live school**           | Last measurement within 21 days                                          | Device actively reporting                                              |
| **At-risk school**        | Last measurement 22-28 days ago                                          | May drop off without follow-up                                         |
| **Drop-off**              | No measurement in 29+ days                                               | Unlikely to return without a site visit                                |
| **Drop-off rate**         | Drop-offs ÷ total installed schools                                      | Above 10% = increase follow-up effort                                  |

For full definitions of every field in the dashboard, see [Metric Glossary](../../installation/metric-glossary.md).

**Output:** Metric reference document circulated to all data users before the first review meeting.

{% hint style="info" %}
**Metric reference - \[Country]**\
Download speed: what it measures / country context / threshold for concern\
Upload speed: what it measures / country context / threshold for concern\
Latency: what it measures / country context / threshold for concern\
Uptime: what it measures / country context / threshold for concern
{% endhint %}

***

### Step 5 - Define KPIs

Translate the use case into 3-5 measurable KPIs, each with a formula, threshold, owner, and review frequency. Keep the KPI set small enough to be actionable; a list of 15 indicators will not be reviewed consistently.

**Each KPI needs:**

| Field                | Description                                 |
| -------------------- | ------------------------------------------- |
| **Name**             | Short, descriptive label                    |
| **Formula**          | Exactly how the number is calculated        |
| **Threshold**        | What counts as "good" vs. "a problem"       |
| **Owner**            | Who monitors and acts on this KPI           |
| **Review cadence**   | How often it is reviewed                    |
| **Action triggered** | What happens when the threshold is breached |

**Examples:**

<details>

<summary>Policy enforcement - % schools meeting national speed benchmark</summary>

|                      |                                                                                                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Formula**          | Schools with 30-day average download speed ≥ \[national threshold] Mbps ÷ total schools with active Giga Meter × 100 |
| **Threshold**        | ≥ 80% on track; < 60% escalate to ISP unit                                                                           |
| **Owner**            | MoE IT Department                                                                                                    |
| **Review cadence**   | Monthly                                                                                                              |
| **Action triggered** | Schools below threshold for 30+ consecutive days reported to ISP coordinator                                         |

</details>

<details>

<summary>ISP performance monitoring - % schools receiving contracted speed</summary>

|                      |                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------- |
| **Formula**          | Schools where measured speed ≥ 80% of contracted Mbps ÷ schools with known contract × 100 |
| **Threshold**        | < 70% compliance = formal notice to ISP                                                   |
| **Owner**            | Procurement / legal unit                                                                  |
| **Review cadence**   | Monthly                                                                                   |
| **Action triggered** | Formal notice to ISP; repeated failure triggers contract review                           |

</details>

<details>

<summary>Deployment health - % installed schools actively reporting</summary>

|                      |                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| **Formula**          | Schools that sent ≥ 1 measurement in the last 7 days ÷ schools with Giga Meter installed × 100 |
| **Threshold**        | < 70% = increase follow-up; < 50% = escalate to Giga                                           |
| **Owner**            | Installation lead                                                                              |
| **Review cadence**   | Weekly for first 3 months, then monthly                                                        |
| **Action triggered** | Contact silent schools; flag persistent drop-offs to Giga                                      |

</details>

Share the completed KPI document with the Giga data team. If your KPIs require dashboard customisation, a column not yet in the standard view, the team will advise on feasibility and timeline.

**Output:** Completed KPI document shared with the Giga data team.

| KPI name | Formula | Threshold | Owner | Review cadence | Action triggered |
| -------- | ------- | --------- | ----- | -------------- | ---------------- |
|          |         |           |       |                |                  |

***

### Step 6 - Set a KPI review and decision-triggering process

Define how often KPIs are reviewed, who runs the review, and what triggers action. Establish this process before the data starts flowing, not after. The most common failure mode is waiting until data exists before deciding what to do with it.

The review format does not need to be elaborate. A standing 30-minute monthly call with a shared dashboard view is more sustainable than a quarterly report that takes two weeks to produce. Countries that define this process upfront are more likely to use Giga Meter data consistently. Countries that leave it informal tend to use the data reactively, only when a crisis prompts them.

**Output:** Document and circulate the review process to all data users before the first data is available.

{% hint style="info" %}
**KPI review process**\
Meeting owner:\
Review cadence: \[weekly / monthly / quarterly]\
Format: \[e.g. standing call, shared dashboard, written brief]\
\
**KPI thresholds and triggers**\
\[KPI name] - threshold: \[value] - action: \[what happens]\
\[KPI name] - threshold: \[value] - action: \[what happens]\
\[KPI name] - threshold: \[value] - action: \[what happens]
{% endhint %}

***

### Step 7 - Build capacity for ongoing analysis

Over time, government teams should be able to produce their own analyses without Giga support: school-level connectivity briefs, ISP performance comparisons, regional coverage reports, and trend analysis over time.

Start small. In the first year, the goal is for the team to answer basic questions from the dashboard independently, which schools are performing well, which have dropped off, and whether the situation has improved since the last review. Deeper analytical capability, such as regression analysis, custom indicators, and API-based reporting, can follow as familiarity grows.

If deeper support is needed at any stage, contact the Giga data team.

**Output:** After 6-12 months, government users can produce and interpret analyses independently without prompting from Giga.

{% hint style="info" %}
**Capacity milestone - \[Date]**\
Team can independently access and filter dashboard: Yes / No\
Team has produced at least one connectivity brief: Yes / No\
Team has reviewed ISP performance data: Yes / No\
Analytical support still needed from Giga: \[describe if applicable]
{% endhint %}

***

### Related pages

* [Government Onboarding Guide](government-onboarding-overview.md)
* [Deployment Blueprint](deployment-blueprint.md)
* [Installation Lead Guide](installation-lead.md)
* [Using the Dashboard](../../country-deployment/using-the-dashboard.md)
* [Metric Glossary](../../installation/metric-glossary.md)
* [Measurement Protocols](../technical-reference/measurement-protocols.md)
* [Data Governance & Privacy](../technical-reference/data-governance.md)
