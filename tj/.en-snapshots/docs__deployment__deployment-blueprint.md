# Deployment Blueprint

Complete this worksheet before the rollout begins. The worksheet is intended to align the implementing team and Giga on strategy, scope, and success criteria, and becomes your shared reference document throughout the deployment.

***

### 1. Country and deployment context

{% hint style="info" %}
**Lead Ministry / Agency:**\
\
**Supporting Ministry / Agency:**\
\
**Deployment rationale** - What is the main goal for deploying Giga Meter?\
• _e.g. create baseline data, track progress against a policy, monitor provider performance_\
\
**Existing monitoring tools** - Are there tools currently used to measure school connectivity?\
\
**National strategy alignment** - How does this fit into broader national digital education or ICT plans? Are there policies or standards defining minimum connectivity for schools?\
\
**School connectivity model** - How is school internet procured, centrally by the ministry or by individual schools?
{% endhint %}

***

### 2. Installation planning

{% hint style="info" %}
**Deployment scope** - Target number and type of schools:\
\
**Phasing** - Pilot cohort size and criteria, then scale-up phases:\
\
**Installation lead** - Who is responsible for coordinating installations?\
• _e.g. MoE IT unit, regional coordinators_\
\
**School IDs** - Do schools and installers have access to official school IDs? If not, how will this be resolved?\
\
**Device availability** - Are Windows devices regularly used and connected to the internet in target schools?\
\
**Training and support** - How will installers be trained? What support channel will be available?\
• _e.g. Zoom webinar, WhatsApp group, hotline_\
\
**School communication** - Is there a centralised channel or contact list for reaching schools?\
\
**Timeline** - Anticipated start and end dates for each phase:
{% endhint %}

***

### 3. Maintenance and support

{% hint style="info" %}
**Champion** - Who inside the ministry (or a partner organisation) will advocate for the data and keep the deployment active?\
\
**School focal points** - How will school-level focal points be assigned and maintained?\
\
**Regional coordination** - Is there a regional coordinator structure? If so, who are the leads?\
\
**Post-installation support** - Who manages troubleshooting after rollout? What is the escalation path to Giga?\
\
**Sustainability plan** - How will monitoring be sustained beyond the initial rollout?\
• _e.g. community of practice, standing review meeting, reinstallation protocol_
{% endhint %}

***

### 4. Data use and ownership

{% hint style="info" %}
**Primary data users** - Who will use the data and for what purposes?\
• _e.g. MoE planning unit for ISP contract review, regional offices for school support prioritisation_\
\
**Access channels** - How will users access the data?\
• _e.g. Giga Maps dashboard, API, exported reports_\
\
**Use case** - What specific decision or action will Giga Meter data inform?\
• _See_ [_Data Analysis Lead Guide - Step 1_](data-analysis-lead.md)\
\
**Analytical support needs** - Will the ministry need support interpreting data, building indicators, or incorporating insights into policy?
{% endhint %}

***

### 5. Success metrics

{% hint style="info" %}
**Short-term success** _(first 3 months)_\
What does success look like?\
\
**Medium-term success** _(1 year)_\
What does success look like?\
\
**Key indicators**\\

* % of target schools with active Giga Meter data\\
* \[Add KPI]\\
* \[Add KPI]
{% endhint %}

***

### 6. Infrastructure and connectivity prerequisites

{% hint style="info" %}
**M-Lab server availability** — Is there an M-Lab NDT7 server inside the country? Check the [M-Lab server map](https://www.measurementlab.net/status/). If there is no local server, speed and latency tests will measure the international path rather than the domestic network. Has this been discussed with the government?\
\
**Data residency** — Does national law or government policy require school connectivity data to be stored on domestic servers or processed within the country?\
\
**Self-hosting** — If data residency requirements apply, is the government considering self-hosting the Giga Meter backend? Self-hosting requires a dedicated technical team (TypeScript, PostgreSQL, Linux DevOps) and two servers. See [Self-Hosting Giga Meter](../technical-reference/self-hosting.md) for full requirements.\
\
**Network reachability** — Have the required network destinations been confirmed open in school and ministry firewalls? See [Network Destinations & Firewall Configuration](../technical-reference/network-destinations.md).
{% endhint %}

***

### Related pages

* [Installation Lead Guide](installation-lead.md)
* [Data Analysis Lead Guide](data-analysis-lead.md)
* [Self-Hosting Giga Meter](../technical-reference/self-hosting.md)
