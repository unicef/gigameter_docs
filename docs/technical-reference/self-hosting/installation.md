# Backend Installation

This guide sets up the Giga Meter backend on a Linux server. Complete this before configuring the Windows app or connecting schools.

{% hint style="warning" %}
The Giga Meter backend is licensed under **AGPL-3.0**. This means the source code is open, you can modify it, but any version you deploy as a network service must also be made available as open source.
{% endhint %}

Linux is the recommended production platform. The backend will run on Windows and macOS for local development, but is not production-tested on those operating systems.

***

### Prerequisites

Before starting, confirm you have:

* **Node.js** 20 or later
* **PostgreSQL** 15 or later
* **Git**
* A server running Ubuntu 22.04 (minimum Ubuntu 18.04) — see [Infrastructure Requirements](infra-requirements.md)

***

### Step 1 — Clone the repository

```bash
git clone https://github.com/unicef/giga-meter-backend.git
cd giga-meter-backend
```

### Step 2 — Install dependencies

```bash
npm install
```

### Step 3 — Configure environment variables

Create a `.env` file in the project root with the following variables:

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string, e.g. `postgresql://user:password@localhost:5432/gigameter` |
| `USE_AUTH` | `true` to require authentication; `false` for open access during testing |
| `PROJECT_CONNECT_SERVICE_URL` | URL of the Giga Maps API used for school lookups |
| `DAILY_CHECK_APP_API_CODE` | API code for the daily check app |
| `PCDC_APP_DOWNLOAD_URL` | URL where the Windows app installer can be downloaded |
| `SENTRY_DSN` | (Optional) Sentry DSN for error tracking |

### Step 4 — Set up the database

Generate the Prisma client and run migrations:

```bash
npx prisma generate
npx prisma migrate dev
```

### Step 5 — Start the server

```bash
npm run start
```

The backend starts at `http://localhost:3000/`. API documentation is available at `/api`.

***

### Authentication

By default, the backend authenticates requests against the Giga Maps API. If you need custom authentication — for example, to integrate with a government identity system — modify `auth.guard.ts` in the source.

***

→ [Docker Setup](docker.md) — alternative deployment using Docker\
→ [Infrastructure Requirements](infra-requirements.md) — server specs\
→ [Unit Testing](unit-testing.md) — validate your setup before going live
