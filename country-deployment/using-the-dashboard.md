# Using the Dashboard

Giga Meter data is published through an [Apache Superset](https://dashboard.giga.global) dashboard. The dashboard is built around three questions: are schools using the app, which schools need attention, and is the internet good enough. This page is a screen-by-screen reference for the current ("v2") dashboard.

For how to get an account and which access channel suits which user, see the [Data Analysis Lead Guide](../docs/deployment/data-analysis-lead.md).

{% hint style="info" %}
**Getting access:** create an account at [dashboard.giga.global](https://dashboard.giga.global), signing in with a Google account (other login options are not yet available). Then share your registered email with the Giga team, who assign you a country-level role. Without a role, you can log in but will not see any data.
{% endhint %}

***

### Dashboard tabs

All tabs are reached from the tab bar at the top of the dashboard. Two of the four tabs are split into sub-tabs of their own — this page refers to those as **Tab > Sub-tab**, e.g. "Monitoring > Summary". Every chart respects the filters set in the left-hand panel — set your country first, then narrow down by date range, region, school, or metric as needed.

| Tab | What it answers |
| --- | --- |
| **Operations** | Are schools installing and using the app? Which schools need follow-up? Covers headline KPIs, the installation funnel, the school-level deployment tracker, and the troubleshooting table. |
| **Monitoring - Summary** | What does current connectivity look like, and how has it trended? Covers headline connectivity KPIs, plus distribution and timeseries charts for download, upload, latency, packet loss, and uptime. |
| **Monitoring - Benchmarking** | Which schools are meeting connectivity targets, and which aren't? Covers pass/fail KPIs, a weekly per-school verdict table, and breakdowns by ISP, region, and connectivity type. |
| **Data Access - Registered Schools** | Which schools are registered, and what's their install/measurement status? One row per registered school. |
| **Data Access - Raw Measurements** | What did each individual speed test record? One row per Giga Meter speed test. |
| **Data Access - School Master** | What reference data exists for each school (location, infrastructure)? One row per registered school. |
| **Data Access - Ping Data** | How reliably is each school staying online, day to day? One row per school and device, per day. |
| **ReadMe** | An in-dashboard quick reference for pages, filters, and definitions. |

Sub-tabs with their own sections below are explained in more detail there — this table is just the map.

<details>

<summary>Operations</summary>

Six headline KPI cards, followed by an installation funnel, a full school-level tracker, and a troubleshooting table for schools that need attention.

<figure><img src="../.gitbook/assets/Superset v2 - Operations Overview.png" alt=""><figcaption></figcaption></figure>

**Headline KPIs**

| What you see | What it means |
| --- | --- |
| Schools installed and active within the last year | Schools sent the Giga Meter app and measured at least once in the last 12 months |
| Target Schools | The installation target for the country (editable via the Target filter — default 3,000) |
| Installed % of Target | Installed-and-active schools as a percentage of the target |
| New Schools This Week | Schools that installed the app for the first time in the last 7 days |
| Actively Measuring Schools | Schools measured on **2 or more distinct days** within the selected lookback window (default 7 days — change it with the Lookback (school days) filter) |
| Schools Mapped | Total schools located and published on Giga Maps, whether or not they run Giga Meter |

**Installation - Activity Funnel and Deployment Health**

Each stage of the funnel is a subset of the one above it, narrowing from the full installed base down to schools measuring most recently.

<figure><img src="../.gitbook/assets/Superset v2 - Operations Funnel.png" alt=""><figcaption></figcaption></figure>

| Funnel stage | What it means |
| --- | --- |
| Mapped | School exists in Giga Maps |
| All installed schools | The Giga Meter app has been sent to the school (this is the funnel's base) |
| Ever measured | The school has sent at least one speed test |
| Measured in last year / 6 months / month / week / today | The school's most recent measurement falls within that window. These are cumulative — a school counted in "last week" is also counted in "last month," "last 6 months," and so on |

Below the funnel, a **Campaign Health** panel classifies every school by its recent measurement pattern (for example: on target, declining, or a sudden stop) so you can spot schools worth a closer look before they show up in Troubleshooting.

**School Deployment Tracker** lists every school with its own row — sorted so the most recently installed schools surface first:

| Column | Definition | Example |
| --- | --- | --- |
| School - ID | School name and Giga school ID | MALIDUWA M.V. - 7113 |
| Region | Administrative region the school sits in | Southern |
| Connectivity | Whether the school is currently marked as connected | Yes |
| Activity tier | Bucket describing how recently/often the school has measured | active_month |
| Installation date | Date the Giga Meter app was installed at the school | 2026-02-02 |
| Days since last activity | Calendar days since the school's last measurement | 7 |
| Tests/working day | Average speed tests run per school day | 0 |
| Pings/working day | Average ping checks run per school day | 0 |
| App version | Giga Meter app version currently running at the school | 2.0.3 |
| Measurements | Total measurements recorded for the school | 109 |

{% hint style="success" %}
Use the Activity Tier and Connectivity filters in the left panel to narrow the tracker to a specific slice of schools, e.g. schools that have gone quiet.
{% endhint %}

**Troubleshooting**

Four alert flags surface schools that likely need a follow-up visit or support call. The four KPI cards above the table double as filters — click a card (e.g. Drop-Off) to filter the table below to just that category, and click it again to clear the filter.

<figure><img src="../.gitbook/assets/Superset v2 - Operations Troubleshooting.png" alt=""><figcaption></figcaption></figure>

| Alert flag | Definition | Recommended action |
| --- | --- | --- |
| Outdated App | At least one device at this school is running an older app version than the newest version seen anywhere in the country | Update app to latest version |
| Inconsistency | The school's measurement frequency has dropped below "Consistent" (roughly 2 or more measurement days a week) during the lookback window — see the regularity breakdown below for the exact wording used | Depends on how sparse the measurements are — see below |
| Location | At least one measurement in the lookback window came from a device location that doesn't match the school's registered GPS coordinates. Only assessed for schools running app v2.0.3 or later | Investigate off-site device usage, or recalibrate GPS |
| Drop-Off | No measurements received in the last **30 school days** — this threshold is fixed and does not change with the Lookback (school days) filter (that filter only affects the other three flags) | Check if app uninstalled or disabled |

Inconsistency's recommended action depends on just how sparse the school's measurements are:

| Measurement regularity | What it means | Recommended action |
| --- | --- | --- |
| Irregular | 1–2 measurement days per week | Check device scheduling and connectivity |
| Monthly only | Less than 1 measurement day per week, but more than one day total in the window | Encourage more frequent app usage |
| Measured once | Exactly one measurement day in the whole window | Confirm device is active and follow up with the school |

{% hint style="info" %}
If more than one flag is active, the Recommended Action column lists every matching action, separated by semicolons. Schools with no active flags show "No action needed."
{% endhint %}

| Column | What it means |
| --- | --- |
| Alert Score | Total number of flags active (0–4), sorted highest first. A score of 2 or more is highlighted red; a score of 1 is highlighted yellow |
| Recommended Action | The suggested next step(s) for this school — see the tables above for the exact wording per flag |
| Days Since Last Measurement | Calendar days since the most recent weekday measurement |
| Oldest Device Version | Oldest app version seen across devices at this school (for drop-off schools, the last known version before they stopped measuring) |
| Total Measurements / Active Days / Daily Std Dev | Calculated within the lookback window; left blank for drop-off schools, since there's no in-window data to evaluate |

{% hint style="info" %}
For schools with no measurements in the lookback window, only the Drop-Off flag can be assessed — the other three columns will be blank rather than "no flag."
{% endhint %}

</details>

<details>

<summary>Monitoring</summary>

Two sub-tabs: **Monitoring > Summary**, for current connectivity quality, and **Monitoring > Benchmarking**, for pass/fail performance against configurable targets.

**Monitoring > Summary**

<figure><img src="../.gitbook/assets/Superset v2 - Monitoring Summary.png" alt=""><figcaption></figcaption></figure>

The four connectivity KPI cards always reflect the **last 5 working days** — this window is fixed and isn't affected by filters. The trend charts below them show weekly data for the last 12 months; use the Date Range filter to narrow that.

| What you see | Definition | What it means |
| --- | --- | --- |
| Download - Mbps | 95th percentile (P95), megabits per second | The download speed that 95% of measurements were at or below — a stable, outlier-resistant read on "typical" performance, calculated across all individual measurements pooled together (not a per-school average) |
| Upload - Mbps | 95th percentile (P95), megabits per second | Same idea as download, for upload speed |
| Latency - ms | 5th percentile (P5), milliseconds | The "best-case" response time — lower is better, so the 5th percentile shows the fast end of the range |
| Packet Loss | 5th percentile (P5), percent | The "best-case" share of data lost in transit — lower is better |
| Uptime - % | Percent | Share of expected ping checks that succeeded |
| Median Daily Pings | Count | Typical number of ping checks a school runs per day |
| Primary Server | — | The most common test server schools in this country connect to |

{% hint style="info" %}
**Why P95?** Independent research into school connectivity data found P95 gives the best balance of stability and sensitivity — it filters out one-off spikes without hiding genuine, sustained changes in speed. It's used here as the standard indicator for "typical" school connectivity.
{% endhint %}

Below the KPI cards is a school search bar to jump to an individual school, plus two views:

| What you see | Chart type | What it means |
| --- | --- | --- |
| Distributions | Histogram | How download, upload, latency, packet loss, and uptime are spread across all schools in the country. Use this to see whether most schools cluster around a similar speed or whether performance is uneven across the country. |
| Timeseries | Weekly trend lines (P95 and median; P95, P5, and median for latency and packet loss) | The same five metrics trending week by week over the last 12 months. Use this to see whether connectivity is improving, holding steady, or declining over time. |

<figure><img src="../.gitbook/assets/Superset v2 - Monitoring Timeseries.png" alt=""><figcaption></figcaption></figure>

**Monitoring > Benchmarking**

<figure><img src="../.gitbook/assets/Superset v2 - Monitoring Benchmarking.png" alt=""><figcaption></figcaption></figure>

Charts on this sub-tab use the Benchmark period filter (default: last 12 months); the school verdict table can also be filtered to one specific week with the Benchmark week filter. Thresholds are adjustable in the left panel — the defaults are 20 Mbps download, 10 Mbps upload, 100 ms latency, and 1% packet loss.

Headline KPI cards at the top of the sub-tab:

| What you see | What it means |
| --- | --- |
| School-weeks passing all benchmarks (last 52 wks) | Share of school-weeks that met all 4 thresholds together |
| % Passing Download (P95) | Share of school-weeks that individually met the download threshold |
| % Passing Upload (P95) | Share of school-weeks that individually met the upload threshold |
| % Passing Latency (P5) | Share of school-weeks that individually met the latency threshold |
| % Passing Packet Loss (P5) | Share of school-weeks that individually met the packet loss threshold |

**How verdicts work:** a school **passes** a given week only if it meets all four benchmark thresholds in its most recent complete week. The **Failure Reason** column in the table shows exactly what caused a fail; use the Verdict Metric filter to isolate schools failing one specific metric.

The **Schools Weekly Benchmark Report** table lists one row per school, per week:

| Column | What it means |
| --- | --- |
| School - ID | School name and Giga school ID |
| ISP | Internet service provider serving the school that week |
| Week Starting | Start date of the benchmark week being evaluated |
| Verdict | Pass or Fail for that school-week, based on all 4 thresholds together |
| Failure Reason | Which metric(s) caused a fail — blank when the school passed |
| Measurements | Number of measurements recorded that week |
| Download - P95 | 95th percentile download speed for that week |
| Upload - P95 | 95th percentile upload speed for that week |
| Latency - P5 | 5th percentile latency for that week |
| Packet Loss - P5 | 5th percentile packet loss for that week |

Below the table, break the same pass/fail picture down **by ISP**, **by Admin Region**, or **by Connectivity Type** — including an ISP Scorecard summarising which providers are hitting benchmark most consistently.

</details>

<details>

<summary>Data Access</summary>

Four raw data tables, each exportable to CSV for offline analysis.

<figure><img src="../.gitbook/assets/Superset v2 - Data Access.png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
To export any table: apply the filters you want, then use the **⋮** menu on the table → **Download** → **CSV**.
{% endhint %}

**Data Access > Registered Schools** — one row per registered school:

| Column | What it means |
| --- | --- |
| school_id_govt | The school's government/national ID |
| school_id_giga | Giga's internal ID for the school |
| sending_gigameter_data | Whether this school has ever sent Giga Meter data |
| first_measurement_date / last_measurement_date | Date of the school's first and most recent measurement |
| days_since_last_measurement | Calendar days since the school's last measurement |
| num_devices_registered / num_devices_measured | Number of devices registered at the school vs. number that have actually sent data |
| max_app_version_gigameter | Newest Giga Meter app version seen at this school |
| install_status | Current installation status (e.g. installed, not installed) |

**Data Access > Raw Measurements** — one row per individual Giga Meter speed test:

| Column | What it means |
| --- | --- |
| download_speed / upload_speed | Measured download/upload speed for this test |
| latency | Round-trip response time for this test |
| packet_loss_rate | Share of data packets lost during this test |
| pass_fail_overall | Whether this individual speed test was technically **valid** — completed, sent enough data, and ran for a sensible duration, checked separately for download and upload. This is a data-quality check on the test itself — separate from the Benchmarking pass/fail verdict (Monitoring > Benchmarking), which checks measured speed against country thresholds |
| reasons_failed_overall | Which check(s) failed, and on which half of the test — e.g. "test incomplete (download)", "insufficient data (upload)", "test too short (download & upload)", "test too long (upload)". Blank when the test passed all checks |
| isp_name | Internet service provider used for this test |
| measurement_time_window | Time-of-day bucket the test was taken in |
| is_weekday | Whether the test was taken on a school day |

**Data Access > School Master** — one row per registered school (reference data):

| Column | What it means |
| --- | --- |
| latitude / longitude | The school's registered coordinates |
| education_level | Primary, secondary, etc. |
| school_area_type | Urban or rural |
| school_funding_type | Public, private, etc. |
| connectivity | Whether the school is currently marked as connected |
| connectivity_type_govt | Connection type as reported by government records |
| cellular_coverage_type | Type of mobile network coverage available at the school (e.g. 3G, 4G) |
| electricity_availability | Whether the school has electricity access |

**Data Access > Ping Data** — one row per school and device, per day. A device is expected to check in roughly every 15 minutes, so across the 8am–8pm school-day window that works out to **48 expected pings per day**. Every column below — records, Uptime, connected, not connected — is scoped to that same 8am–8pm window, not the full day.

| Column | What it means |
| --- | --- |
| records | Number of ping checks actually logged that day (8am–8pm local). Can land below 48 if the device was offline or checking in less often, or above it if it checked in more frequently than expected |
| Uptime | Share of that day's logged checks that succeeded — connected ÷ records. This is measured against the checks actually made, not the fixed 48 expected, so a device with only a handful of checks that day can still show 100% uptime if every one of them succeeded |
| connected / not connected | Count of successful / failed ping checks within the window |
| latency | Average response time for ping checks that day |

</details>

<details>

<summary>ReadMe</summary>

The dashboard's own **ReadMe** tab is the fastest way to check filter definitions or refresh your memory on what a page covers without leaving Superset — it summarises the same pages, lists every filter with a one-line explanation, and notes how the underlying data is refreshed (daily) and scoped (weekdays only, most recent complete week for benchmark verdicts). Worth bookmarking alongside this page.

</details>

***

### Related pages

* [Data Analysis Lead Guide](../docs/deployment/data-analysis-lead.md)
* [Metric Glossary](../get-started/metric-glossary.md)
* [Installation Lead Guide](../docs/deployment/installation-lead.md)
