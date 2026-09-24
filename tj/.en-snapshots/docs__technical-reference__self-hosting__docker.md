# Docker Setup

Docker is an alternative way to run the Giga Meter backend without installing Node.js and PostgreSQL directly on the host.

{% hint style="warning" %}
The Docker configuration for Giga Meter is community-contributed and is **not officially supported** by Giga. Giga will accept bug fixes and documentation improvements, but does not guarantee compatibility or provide support for Docker-based deployments. Use at your own risk.
{% endhint %}

***

### Prerequisites

* Docker installed on the host
* Docker Compose (`docker compose` without a hyphen — the current standard per Docker's official guidance)

***

### Build the image

A [Dockerfile](https://github.com/unicef/giga-meter-backend/blob/58861714ffa21c4eff1ca8ec5e629aba16594dec/Dockerfile) is included in the repository. Build it with:

```bash
docker build -f Dockerfile -t repo:tag .
```

Replace `repo:tag` with your preferred image name and tag.

***

### Run the container

The application runs on port 3000. Pass environment variables with `-e` flags:

```bash
docker run -d -p 3000:3000 \
  -e DATABASE_URL="postgresql://username:password@localhost:5432/pcdc?schema=public" \
  -e DAILY_CHECK_APP_API_CODE="DAILY_CHECK_APP" \
  -e USE_AUTH="true" \
  -e PROJECT_CONNECT_SERVICE_URL="https://your-giga-maps-service-url" \
  -e PCDC_APP_DOWNLOAD_URL="https://your-windows-app-download-url" \
  repo:tag
```

The `-d` flag runs the container in the background. The backend will be available at `http://localhost:3000/`. For all environment variable descriptions, see [Backend Installation](installation.md).

***

→ [Backend Installation](installation.md) — standard (non-Docker) setup\
→ [Unit Testing](unit-testing.md) — validate the deployment
