# Using the Dashboard

Giga Meter data and insights are available at [dashboard.giga.global](https://dashboard.giga.global), powered by Apache Superset.

The dashboard is designed to help answer three questions:

1. **Is Giga Meter installed and measuring as expected?**
2. **Which schools need attention?**
3. **Is school connectivity meeting expectations?**

This page is a screen-by-screen reference for the dashboard. It explains what each tab shows, how key metrics are calculated, and how to interpret the main charts and tables.

### Sign in to the dashboard

Create an account with an email address from any domain; it does not need to be a Google or Microsoft account. A one-time code sent to that address verifies your account.

{% stepper %}
{% step %}
**Open the dashboard**

Open [dashboard.giga.global](https://dashboard.giga.global) and select **Sign in with Azure**.
{% endstep %}

{% step %}
**Create an account**

Select **No account? Create one**, enter your email address, and select **Next**.
{% endstep %}

{% step %}
**Enter the one-time code**

Enter the code sent to your email and select **Next**. Check your spam folder if it does not arrive.
{% endstep %}

{% step %}
**Accept the permissions**

Select **Accept** on the **Permissions requested** screen. The app requests access to your basic profile and to maintain access to data you have authorized. The notice that it is not published by Microsoft is expected.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
**Dashboard access can take up to 2 business days.** New accounts start with an empty home page while the Giga team assigns a country-level role.
{% endhint %}

***

### Dashboard tabs

Use the top tab bar to move between dashboard areas. Monitoring and Data Access contain sub-tabs, shown here as **Tab > Sub-tab** (for example, **Monitoring > Summary**). Filters are in the left panel; choose a country first, then narrow by date, region, school, or metric.

| Tab | What it answers |
| --- | --- |
| **Operations** | App installation, usage, deployment, and schools needing follow-up. |
| **Monitoring > Summary** | Current connectivity and trends in download, upload, latency, packet loss, and uptime. |
| **Monitoring > Benchmarking** | School performance against connectivity targets, by week, ISP, region, and connectivity type. |
| **Data Access > Registered Schools** | Registration and measurement status; one row per school. |
| **Data Access > Raw Measurements** | Results from individual Giga Meter speed tests. |
| **Data Access > School Master** | School reference data, including location and infrastructure. |
| **Data Access > Ping Data** | Daily connectivity by school and device. |
| **ReadMe** | An in-dashboard quick reference for pages, filters, and definitions. |

Expand a section below for its screen-by-screen details.

<details>

<summary>Operations</summary>

Operations combines six headline KPIs, an installation funnel, a school deployment tracker, and troubleshooting alerts.

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

Each stage narrows the installed base to schools measured most recently.

<figure><img src="../.gitbook/assets/Superset v2 - Operations Funnel.png" alt=""><figcaption></figcaption></figure>

| Funnel stage | What it means |
| --- | --- |
| Mapped | School exists in Giga Maps |
| All installed schools | The Giga Meter app has been sent to the school (this is the funnel's base) |
| Ever measured | The school has sent at least one speed test |
| Measured in last year / 6 months / month / week / today | Most recent measurement falls in that period. Periods are cumulative: last-week schools also count in last month, 6 months, and year |

**School Deployment Tracker** lists one row per school, with the most recently installed first:

<figure><img src="../.gitbook/assets/Superset v2 - Operations Deployment Tracker.png" alt=""><figcaption></figcaption></figure>

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
Use the Activity Tier and Connectivity filters to find schools that need follow-up, such as schools that have gone quiet.
{% endhint %}

**Troubleshooting**

Four alert flags identify schools that may need support. Select a KPI card to filter the table by that flag; select it again to clear the filter.

**Troubleshooting KPIs**

<figure><img src="../.gitbook/assets/Superset v2 - Operations Troubleshooting.png" alt=""><figcaption></figcaption></figure>

| Alert flag | Definition | Recommended action |
| --- | --- | --- |
| Outdated App | A device at the school runs an older version than the latest version seen in the country | Update the app |
| Inconsistency | Measurement frequency fell below roughly 2 days per week during the lookback window | See regularity actions below |
| Location | A recent measurement location differs from the school's registered coordinates. Available for app v2.0.3 and later | Check off-site use or recalibrate GPS |
| Drop-Off | No measurement in the last **30 school days**. This fixed threshold is not affected by the Lookback filter | Check whether the app is installed and enabled |

For Inconsistency, choose an action based on measurement frequency:

| Measurement regularity | What it means | Recommended action |
| --- | --- | --- |
| Irregular | 1–2 measurement days per week | Check device schedule and connectivity |
| Monthly only | Fewer than 1 day per week, but more than one day in the window | Encourage more frequent app use |
| Measured once | Exactly one measurement day in the whole window | Confirm device is active and follow up with the school |

{% hint style="info" %}
When multiple flags are active, Recommended Action lists each action. Schools without flags show "No action needed."
{% endhint %}

**School Troubleshooting Table** lists one row per flagged school:

<figure><img src="../.gitbook/assets/Superset v2 - Operations Troubleshooting Table.png" alt=""><figcaption></figcaption></figure>

| Column | What it means |
| --- | --- |
| Alert Score | Number of active flags (0–4), highest first; 2+ is red and 1 is yellow |
| Recommended Action | Suggested next step for each active flag |
| Days Since Last Measurement | Days since the latest weekday measurement |
| Oldest Device Version | Oldest version at the school; for drop-off schools, the last version seen before measurements stopped |

{% hint style="info" %}
With no measurements in the lookback window, only Drop-Off can be assessed; the other flags are blank.
{% endhint %}

</details>

<details>

<summary>Monitoring > Summary</summary>

Summary shows current connectivity KPIs and trends for download, upload, latency, packet loss, and uptime.

<figure><img src="../.gitbook/assets/Superset v2 - Monitoring Summary.png" alt=""><figcaption></figcaption></figure>

The four connectivity KPI cards cover the **last 5 working days** and are not affected by filters. Trend charts show weekly data for the last 12 months; use Date Range to narrow the period.

| What you see | Definition | What it means |
| --- | --- | --- |
| Download - Mbps | 95th percentile (P95), Mbps | Download speed at or below which 95% of measurements fall, pooled across measurements rather than averaged by school |
| Upload - Mbps | 95th percentile (P95), Mbps | Upload speed at or below which 95% of measurements fall |
| Latency - ms | 5th percentile (P5), ms | Response time near the fast end of the range; lower is better |
| Packet Loss | 5th percentile (P5), percent | Packet loss near the low end of the range; lower is better |
| Uptime - % | Percent | Successful ping checks as a share of expected checks |
| Median Daily Pings | Count | Typical ping checks per school per day |
| Primary Server | Most measurements over the past 365 days | The server most used in the country. This uses a fixed 365-day window and is not affected by Date Range. |

{% hint style="info" %}
**Why P95?** Independent research into school connectivity data found P95 gives the best balance of stability and sensitivity — it filters out one-off spikes without hiding genuine, sustained changes in speed. It's used here as the standard indicator for "typical" school connectivity.
{% endhint %}

Search for a school below the KPIs, or explore these views:

| What you see | Chart type | What it means |
| --- | --- | --- |
| Distributions | Histogram | How download, upload, latency, packet loss, and uptime vary across the country |
| Timeseries | Weekly trend lines | Trends in the five metrics over the last 12 months; percentiles shown vary by metric |

**Distributions**

<figure><img src="../.gitbook/assets/Superset v2 - Monitoring Distributions.png" alt=""><figcaption></figcaption></figure>

**Timeseries**

<figure><img src="../.gitbook/assets/Superset v2 - Monitoring Timeseries.png" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary>Monitoring > Benchmarking</summary>

Benchmarking compares school connectivity with configurable targets, by week, school, ISP, region, and connectivity type.

<figure><img src="../.gitbook/assets/Superset v2 - Monitoring Benchmarking.png" alt=""><figcaption></figcaption></figure>

Use Benchmark period (default: 12 months) to filter charts and Benchmark week to select a week in the school table. Adjust thresholds in the left panel. Defaults: 20 Mbps download, 10 Mbps upload, 100 ms latency, and 1% packet loss.

Headline KPI cards at the top of the sub-tab:

| What you see | What it means |
| --- | --- |
| School-weeks passing all benchmarks (last 52 wks) | Share of school-weeks that met all 4 thresholds together |
| % Passing Download (P95) | Share of school-weeks that individually met the download threshold |
| % Passing Upload (P95) | Share of school-weeks that individually met the upload threshold |
| % Passing Latency (P5) | Share of school-weeks that individually met the latency threshold |
| % Passing Packet Loss (P5) | Share of school-weeks that individually met the packet loss threshold |

**Verdicts:** A school passes its most recent complete week only when it meets all four thresholds. Failure Reason identifies unmet thresholds; use Verdict Metric to filter by metric.

**Pass / Fail Over Time** shows weekly counts of passing (green) and failing (red) schools:

<figure><img src="../.gitbook/assets/Superset v2 - Monitoring Benchmarking Pass Fail.png" alt=""><figcaption></figcaption></figure>

**Schools Weekly Benchmark Report** lists one row per school per week:

<figure><img src="../.gitbook/assets/Superset v2 - Monitoring Benchmarking Report.png" alt=""><figcaption></figcaption></figure>

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

Below the table, view pass rates by ISP, Admin Region, or Connectivity Type.

**By ISP** — the scorecard compares providers' pass rates and typical performance:

<figure><img src="../.gitbook/assets/Superset v2 - Monitoring Benchmarking By ISP.png" alt=""><figcaption></figcaption></figure>

| Column | What it means |
| --- | --- |
| isp_name | Internet service provider |
| schools_served | Number of schools using this ISP |
| pct_passing_benchmark | Share of school-weeks passing all four thresholds |
| p95_download_mbps / p95_upload_mbps | 95th percentile download/upload speed |
| p5_latency_ms / p5_packet_loss_pct | 5th percentile latency/packet loss |

**By Admin Region** shows each region's share of school-weeks passing benchmark.

<figure><img src="../.gitbook/assets/Superset v2 - Monitoring Benchmarking By Admin.png" alt=""><figcaption></figcaption></figure>

**By Connectivity Type** groups the pass-rate breakdown by each school's registered connection type.

</details>

Data Access contains four tables, each exportable to CSV.

{% hint style="success" %}
To export a table, apply filters, then select **⋮ > Download > CSV**.
{% endhint %}

<details>

<summary>Data Access > Registered Schools</summary>

One row per registered school.

<figure><img src="../.gitbook/assets/Superset v2 - Data Access Registered Schools.png" alt=""><figcaption></figcaption></figure>

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

</details>

<details>

<summary>Data Access > Raw Measurements</summary>

One row per Giga Meter speed test.

<figure><img src="../.gitbook/assets/Superset v2 - Data Access Raw Measurements.png" alt=""><figcaption></figcaption></figure>

| Column | What it means |
| --- | --- |
| download_speed / upload_speed | Measured download/upload speed for this test |
| latency | Round-trip response time for this test |
| packet_loss_rate | Share of data packets lost during this test |
| pass_fail_overall | Whether the test was technically valid (complete, sufficient data, sensible duration). This data-quality check is separate from the benchmark verdict, which compares results with thresholds |
| reasons_failed_overall | Failed validity check and test direction; blank when all checks passed |
| isp_name | Internet service provider used for this test |
| measurement_time_window | Time-of-day bucket the test was taken in |
| is_weekday | Whether the test was taken on a school day |

</details>

<details>

<summary>Data Access > School Master</summary>

One row per registered school (reference data):

<figure><img src="../.gitbook/assets/Superset v2 - Data Access School Master.png" alt=""><figcaption></figcaption></figure>

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

</details>

<details>

<summary>Data Access > Ping Data</summary>

Devices are expected to check in every 15 minutes: **48 expected pings per school day** (8am–8pm). All counts and uptime below use this window.

<figure><img src="../.gitbook/assets/Superset v2 - Data Access Ping Data.png" alt=""><figcaption></figcaption></figure>

| Column | What it means |
| --- | --- |
| records | Ping checks logged that day; may be below or above 48 depending on device activity |
| Uptime | Successful checks ÷ logged checks. It uses actual checks, so a few successful checks can still show 100% |
| connected / not connected | Count of successful / failed ping checks within the window |
| latency | Average response time for ping checks that day |

</details>

<details>

<summary>ReadMe</summary>

The **ReadMe** tab summarizes dashboard pages and filters, and explains data refresh (daily) and scope (weekdays; benchmark verdicts use the latest complete week).

</details>

***

### Related pages

* [Data Analysis Lead Guide](../docs/deployment/data-analysis-lead.md)
* [Metric Glossary](../get-started/metric-glossary.md)
* [Installation Lead Guide](../docs/deployment/installation-lead.md)
