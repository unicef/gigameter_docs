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

```bash
docker build -f Dockerfile -t gigameter-backend:latest .
```

Replace `gigameter-backend:latest` with your preferred image name and tag.

***

### Run the container

```bash
docker run -p 3000:3000 \
  -e DATABASE_URL="postgresql://user:password@host:5432/gigameter" \
  -e DAILY_CHECK_APP_API_CODE="your_api_code" \
  -e PCDC_APP_DOWNLOAD_URL="https://your-download-url" \
  -e PROJECT_CONNECT_SERVICE_URL="https://your-giga-maps-api" \
  -e USE_AUTH=true \
  gigameter-backend:latest
```

The backend will be available at `http://localhost:3000/`. For all environment variable descriptions, see [Backend Installation](installation.md).

***

→ [Backend Installation](installation.md) — standard (non-Docker) setup\
→ [Unit Testing](unit-testing.md) — validate the deployment
