# Self-Hosting Giga Meter

By default, Giga Meter sends measurement data to Giga's hosted backend at `meter.giga.global`. Self-hosting means running your own instance of the backend on national or government-managed infrastructure, so that data is stored and processed within the country.

Self-hosting is available as a **beta feature** under the [AGPL-3.0 licence](https://www.gnu.org/licenses/agpl-3.0.en.html). For most deployments, the hosted Giga backend is the faster, lower-maintenance path. Self-hosting adds significant technical overhead and ongoing responsibility for your team.

***

### When self-hosting is relevant

Consider self-hosting if:

* National law or policy requires school data to be stored on domestic servers
* The government wants an independent record of measurements outside Giga's platform
* Your team has the capacity to deploy and maintain a Node.js/PostgreSQL application in production

***

### What's involved

Before committing to self-hosting, read these two pages:

* [Developer Requirements](self-hosting/dev-skillset.md) — TypeScript, PostgreSQL, Linux DevOps skills your team needs
* [Infrastructure Requirements](self-hosting/infra-requirements.md) — server specs to provision (two servers: app + database)

***

### Setup guides

Once prerequisites are in place:

1. [Backend Installation](self-hosting/installation.md) — standard setup with Node.js and PostgreSQL
2. [Docker Setup](self-hosting/docker.md) — alternative deployment via Docker (community-contributed, not officially supported)
3. [Windows App Setup](self-hosting/windows-app.md) — configure the Windows app to use your backend and customise branding
4. [Unit Testing](self-hosting/unit-testing.md) — validate the deployment before connecting schools

***

### Related pages

* [Deployment Blueprint](../deployment/deployment-blueprint.md) — includes questions to answer before committing to a deployment model
* [Network Destinations & Firewall Configuration](network-destinations.md) — required endpoints for the hosted backend
