# Backend Installation

The Giga Meter backend can be deployed in multiple ways. This guide covers the standard Node.js setup. For Docker, see [Docker Setup](docker.md). The source repository is [unicef/giga-meter-backend](https://github.com/unicef/giga-meter-backend).

{% hint style="warning" %}
**AGPL-3.0 licence**

The Giga Meter backend is licensed under AGPL-3.0. Three clauses apply to anyone self-hosting:

* **Access to Source Code** — users who download and self-host are entitled to the complete corresponding source code.
* **Network Interaction Clause** — if you modify and host a version for others to use over a network, you must make your modified source code available to those users.
* **Freedom to Modify and Share** — once you download and self-host, you are free to modify the software and share it, provided you comply with AGPL-3.0.

Full licence text: [gnu.org/licenses/agpl-3.0.en.html](https://www.gnu.org/licenses/agpl-3.0.en.html)
{% endhint %}

Linux is the recommended production platform. The backend will run on Windows and macOS for local development, but is not production-tested on those operating systems.

***

### Requirements

The backend has minimal hardware requirements on its own. The most intensive part is database query load as measurement volume grows. See [Infrastructure Requirements](infra-requirements.md) for server specs.

Before starting, confirm:

* **Node.js** 20 or later
* **PostgreSQL** 15 or later
* **Git**
* Ubuntu 22.04 recommended (Ubuntu 18.04 minimum)

***

### Step 1 — Clone the repository

```bash
git clone https://github.com/unicef/giga-meter-backend.git
cd giga-meter-backend
```

Then install dependencies:

```bash
npm install
```

***

### Step 2 — Configure environment variables

Create a `.env` file in the project root with the following variables:

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string, e.g. `postgresql://username:password@localhost:5432/pcdc?schema=public` |
| `USE_AUTH` | Set `"true"` if APIs should require authentication; `"false"` for open access during testing |
| `PROJECT_CONNECT_SERVICE_URL` | Base URL of the Giga Maps service API used for authentication |
| `DAILY_CHECK_APP_API_CODE` | API code for the daily check app used in calling the Giga Maps service API. The placeholder value is `DAILY_CHECK_APP` |
| `PCDC_APP_DOWNLOAD_URL` | Download URL for the latest version of the Windows application |
| `SENTRY_DSN` | (Optional) Sentry DSN for error tracking |

{% hint style="info" %}
`PROJECT_CONNECT_SERVICE_URL` and `DAILY_CHECK_APP_API_CODE` are only required if you want to use the built-in Giga Meter authentication (`USE_AUTH="true"`).
{% endhint %}

Full `.env` example:

```
DATABASE_URL="postgresql://username:password@localhost:5432/pcdc?schema=public"
USE_AUTH="true"
PROJECT_CONNECT_SERVICE_URL="https://your-giga-maps-service-url"
DAILY_CHECK_APP_API_CODE="DAILY_CHECK_APP"
PCDC_APP_DOWNLOAD_URL="https://your-windows-app-download-url"
SENTRY_DSN="your-sentry-dsn"
```

***

### Step 3 — Set up the database

Once `DATABASE_URL` is set, generate the Prisma client. Run this command **inside the `src/prisma` folder**:

```bash
npx prisma generate
```

***

### Step 4 — Run database migrations

Make any required changes to `prisma.schema` (located inside `src/prisma`), then run migrations. Run this command **inside the `src/prisma` folder**:

```bash
npx prisma migrate dev
```

***

### Step 5 — Start the server

From the project root:

```bash
npm run start
```

The app runs at `http://localhost:3000/`. Swagger UI is available at `/api`. To list all API routes, navigate to `/api/all`.

***

### Authentication

To enable authentication, set `USE_AUTH="true"` in your `.env` file:

```
USE_AUTH="true"
```

The default authentication validates requests against the Giga Maps service API using a generated API key. The implementation is in [`auth.guard.ts`](https://github.com/unicef/giga-meter-backend/blob/58861714ffa21c4eff1ca8ec5e629aba16594dec/src/auth/auth.guard.ts#L15).

To use custom authentication — for example, to integrate with a government identity system — update the logic in `auth.guard.ts`. Refer to the [NestJS authentication documentation](https://docs.nestjs.com/security/authentication#implementing-the-authentication-guard) for implementation patterns.

***

→ [Docker Setup](docker.md) — alternative deployment using Docker\
→ [Infrastructure Requirements](infra-requirements.md) — server specs\
→ [Unit Testing](unit-testing.md) — validate your setup before going live
