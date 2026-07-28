# Developer Requirements

Self-hosting Giga Meter requires a technical team capable of deploying, maintaining, and modifying a Node.js application in production. This page describes the skill set needed.

If your team does not have these skills in-house, consider whether self-hosting is the right path — the standard hosted Giga backend removes this overhead entirely.

***

### Skills required

**Full-stack TypeScript**
The backend is built with NestJS and the Windows app frontend with Angular. Tailwind CSS is used for styling.

* [Angular](https://angular.dev/) — frontend framework (Windows app)
* [NestJS](https://nestjs.com/) — backend framework
* Tailwind CSS — styling

**Database**
The app uses PostgreSQL with Prisma as the ORM. Your team should be comfortable with:

* PostgreSQL basics — schema, queries, migrations
* Prisma — generating clients, running migrations, understanding the schema

**DevOps**
Running this in production requires:

* Linux server management (Ubuntu 22.04 recommended)
* Deployment and process management (e.g. PM2, systemd)
* Basic networking and security — HTTPS configuration, firewall rules, port management

***

→ [Infrastructure Requirements](infra-requirements.md) — server specs to provision\
→ [Backend Installation](installation.md) — setup steps
