# Infrastructure Requirements

A self-hosted Giga Meter deployment requires two servers: one for the application and one for the database. They can be separate VMs or, for smaller deployments, co-hosted on one machine — though separation is recommended for production.

Ubuntu 22.04 is recommended. Ubuntu 18.04 is the minimum supported version.

***

### Server specifications

| Component | CPU | RAM | Storage |
|---|---|---|---|
| **Application server** | 2–4 vCPUs | 4–8 GB | 20–40 GB SSD |
| **Database server** (PostgreSQL) | 2–4 vCPUs | 4–8 GB | 50–100 GB SSD |

Storage requirements grow over time as measurement volume increases. Size toward the higher end if you are deploying across a large number of schools or expect rapid scale-up.

***

### Software dependencies

| Dependency | Minimum version | Recommended |
|---|---|---|
| Node.js | 20 | Latest LTS |
| PostgreSQL | 15 | Latest stable |
| OS | Ubuntu 18.04 | Ubuntu 22.04 |

***

### Networking

* **HTTPS** — all traffic to the backend must be encrypted. Use a reverse proxy (e.g. nginx) with a valid TLS certificate.
* **Port access** — restrict inbound access to only the ports required (typically 443 for HTTPS, 22 for SSH management).
* **Firewall** — the application server needs outbound access to the Giga Maps API and Sentry (if error tracking is enabled).

***

→ [Developer Requirements](dev-skillset.md) — team skills needed\
→ [Backend Installation](installation.md) — setup steps once infrastructure is ready
