# Measurement Protocols

Giga Meter uses two tests to assess internet quality at schools: a speed test and a ping test.

***

### Speed test

The speed test uses the NDT7 protocol, developed, maintained, and hosted by [Measurement Lab (M-Lab)](https://www.measurementlab.net/). It measures download and upload speeds at scheduled intervals against the nearest M-Lab server.

{% hint style="info" %}
Earlier versions of Giga Meter used the NDT5 protocol. As of version 2.0, all measurements use NDT7.
{% endhint %}

**What it measures:**

* Download speed (Mbps)
* Upload speed (Mbps)
* Latency (ms)

***

### Ping test

_Introduced in version 2.0.2, November 2025._

The ping test runs every 15 minutes during school hours (8am-8pm local time) against the nearest Cloudflare server.

**What it measures:**

* Whether the device has internet connectivity at that point in time
* **Uptime** - the percentage of successful ping responses out of total attempts on powered-on devices during school hours

***

### Measurement schedule

| Test type       | Frequency        | Window                                                                       |
| --------------- | ---------------- | ---------------------------------------------------------------------------- |
| **Speed test**  | Up to 4 per day  | First test within 15 min of device power-on; remaining tests in 3 time slots |
| **Ping test**   | Every 15 minutes | 8am-8pm local time                                                           |
| **Manual test** | On demand        | Any time                                                                     |

**Speed test time slots** (based on system local time):

| Slot      | Time     |
| --------- | -------- |
| Morning   | 8am-12pm |
| Afternoon | 12pm-4pm |
| Evening   | 4pm-8pm  |

{% hint style="info" %}
Tests do not run when the device is switched off or in sleep mode. For best results, keep the device on and connected to the school's internet through the day.
{% endhint %}

***

### Measurement servers

#### Speed test servers (NDT7 / M-Lab)

Giga Meter does not use a fixed test server. For each speed test, it selects the nearest available M-Lab server using M-Lab's Locate API:

1. The app calls `locate.measurementlab.net` and requests the nearest NDT server
2. The Locate API returns the hostname of the nearest available server based on network routing
3. The app connects to that server over WebSocket/TLS on port 443 and runs the NDT7 test

Because the server is selected at runtime, the same school may test against different servers on different runs, particularly if M-Lab adds, removes, or takes servers offline for maintenance. The `ServerInfo` field in each measurement record identifies which server was used.

**M-Lab server tiers:**

| Tier                     | Description                                                                 |
| ------------------------ | --------------------------------------------------------------------------- |
| Cloud deployments        | Cloud-hosted, managed by M-Lab                                              |
| Full site deployments    | Multiple co-located servers at a single point of presence, managed by M-Lab |
| Minimal site deployments | Single server at a point of presence, managed by M-Lab                      |

For network whitelisting, the wildcard `*.measurementlab.net` covers all tiers. A static IP list is not feasible and is not maintained, because M-Lab's server pool changes regularly.

**Why the server choice affects results:**

The M-Lab server is the remote endpoint for the speed test. A closer server (fewer hops, lower latency) generally allows TCP to reach higher throughput than a distant one. Giga Meter selects the nearest server to reduce this variable, but cross-border routing means a school near a border may sometimes test against a server in a neighbouring country. The `ServerInfo.Country` field in the API response shows where the selected server is located.

#### Ping / uptime test server (Cloudflare)

The uptime ping test targets `speed.cloudflare.com`. Unlike M-Lab, this is a fixed target: Cloudflare's anycast network routes the connection to the nearest Cloudflare data centre automatically. The uptime metric reflects whether the device can reach the public internet, not connectivity to any specific server.

***

### Connectivity status on Giga Maps

Giga Meter results classify school connectivity status on [Giga Maps](https://maps.giga.global/):

| Colour    | Status                                       |
| --------- | -------------------------------------------- |
| 🟢 Green  | Good connectivity (meets selected benchmark) |
| 🟡 Yellow | Moderate connectivity                        |
| 🔴 Red    | Slow connectivity (below selected benchmark) |
| 🔵 Blue   | No recent data                               |
