# Self-Hosting Giga Meter

By default, Giga Meter sends all measurement data to Giga's hosted backend at `meter.giga.global`. Self-hosting means deploying your own instance of the backend on national or government-managed infrastructure, so that data is stored and processed within the country before (or instead of) being sent to Giga.

Self-hosting is available as a **beta feature** under the [AGPL-3.0 licence](https://www.gnu.org/licenses/agpl-3.0.en.html). Official support is limited — governments considering this path should discuss feasibility with their technical team before committing.

Full technical documentation: [meter.giga.global/self-hosting](https://meter.giga.global/self-hosting)

***

### When self-hosting is relevant

Self-hosting is worth considering if:

* National law or policy requires school data to be stored on domestic servers
* The government wants an independent record of measurements outside Giga's platform
* The country has the technical capacity to deploy and maintain a Node.js/PostgreSQL application

For most deployments, the hosted Giga backend is the faster, lower-maintenance path. Self-hosting adds significant technical overhead and ongoing responsibility.

***

### What self-hosting requires

#### Developer skills

A team capable of maintaining a self-hosted instance needs:

* **Full-stack TypeScript** — Angular (frontend), NestJS (backend), Tailwind CSS
* **Database** — PostgreSQL basics, experience with ORMs (the app uses Prisma)
* **DevOps** — Linux server management, deployment and process management, basic networking and security

#### Infrastructure

Two servers are required — one for the application and one for the database. Both should run Ubuntu 22.04 (minimum Ubuntu 18.04).

| Component | CPU | RAM | Storage |
|---|---|---|---|
| Application server | 2–4 vCPUs | 4–8 GB | 20–40 GB SSD |
| Database server (PostgreSQL) | 2–4 vCPUs | 4–8 GB | 50–100 GB SSD |

Additional requirements: HTTPS, Node.js 20+, PostgreSQL 15+.

***

### Deployment options

**Standard (recommended)**
Clone the backend repository, configure environment variables, run database migrations with Prisma, and start the server. Linux is the recommended production platform.

```
git clone https://github.com/unicef/giga-meter-backend.git
npm install
npx prisma migrate dev
npm run start
```

Full guide: [meter.giga.global/self-hosting/installation](https://meter.giga.global/self-hosting/installation)

**Docker (community-contributed)**
A Docker Compose configuration is available but is not officially supported by Giga. Use at your own risk.

Full guide: [meter.giga.global/self-hosting/docker](https://meter.giga.global/self-hosting/docker)

***

### Authentication

The default configuration uses Giga Maps API for authentication. Governments that need custom authentication can modify `auth.guard.ts` in the backend source.

***

### Related pages

* [Deployment Blueprint](../deployment/deployment-blueprint.md) — questions to answer before committing to a deployment model
* [Network Destinations & Firewall Configuration](network-destinations.md) — required endpoints for the hosted backend
* [Measurement Protocols](measurement-protocols.md) — how tests work regardless of backend configuration
