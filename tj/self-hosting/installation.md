# Насби бэкенд

Бэкенди Giga Meter метавонад бо якчанд роҳ ҷойгир карда шавад. Ин дастур насбкунии стандартии Node.js-ро дар бар мегирад. Барои Docker ба [Насби Docker](docker.md) нигаред. Анбори манбаъ [unicef/giga-meter-backend](https://github.com/unicef/giga-meter-backend) мебошад.

{% hint style="warning" %}
**Литсензияи AGPL-3.0**

Бэкенди Giga Meter тибқи литсензияи AGPL-3.0 паҳн карда мешавад. Барои ҳар кас, ки худаш онро мизбонӣ мекунад (self-host), се шарт татбиқ мегардад:

* **Дастрасӣ ба рамзи манбаъ** — корбароне, ки барномаро боргирӣ карда, худашон мизбонӣ мекунанд, ҳуқуқ доранд ба рамзи пурраи манбаи мувофиқ дастрасӣ дошта бошанд.
* **Шарти ҳамкории шабакавӣ** — агар Шумо нусхаро тағйир дода, барои истифодаи дигарон тавассути шабака мизбонӣ кунед, бояд рамзи манбаи тағйирёфтаи худро ба ин корбарон дастрас созед.
* **Озодии тағйир додан ва мубодила кардан** — пас аз боргирӣ ва мизбонии мустақил, Шумо метавонед барномаро тағйир дода, паҳн кунед, ба шарте ки талаботи AGPL-3.0-ро риоя намоед.

Матни пурраи литсензия: [gnu.org/licenses/agpl-3.0.en.html](https://www.gnu.org/licenses/agpl-3.0.en.html)
{% endhint %}

Linux платформаи тавсияшуда барои истеҳсолот мебошад. Бэкенд дар Windows ва macOS барои таҳияи маҳаллӣ кор мекунад, аммо дар ин системаҳои амалиётӣ барои истифодаи истеҳсолӣ санҷида нашудааст.

***

### Талабот

Бэкенд худаш талаботи ками сахтафзорӣ дорад. Қисми аз ҳама вазнинтарин бор ба пойгоҳи додаҳо ҳангоми зиёд шудани ҳаҷми ченкуниҳо мебошад. Барои хусусиятҳои сервер ба [Талаботи инфрасохтор](infra-requirements.md) нигаред.

Пеш аз оғоз, инҳоро санҷед:

* **Node.js** 20 ё баландтар
* **PostgreSQL** 15 ё баландтар
* **Git**
* Ubuntu 22.04 тавсия дода мешавад (ҳадди ақал Ubuntu 18.04)

***

### Қадами 1 — Клон кардани анбор

```bash
git clone https://github.com/unicef/giga-meter-backend.git
cd giga-meter-backend
```

Сипас вобастагиҳоро насб кунед:

```bash
npm install
```

***

### Қадами 2 — Танзими тағйирёбандаҳои муҳит

Дар решаи лоиҳа файли `.env`-ро бо тағйирёбандаҳои зерин созед:

| Тағйирёбанда | Тавсиф |
|---|---|
| `DATABASE_URL` | Сатри пайвастшавӣ ба PostgreSQL, масалан `postgresql://username:password@localhost:5432/pcdc?schema=public` |
| `USE_AUTH` | Агар API-ҳо бояд санҷиши ҳаққонияти (аутентификатсия) талаб кунанд, `"true"`-ро гузоред; барои дастрасии кушода ҳангоми санҷиш — `"false"` |
| `PROJECT_CONNECT_SERVICE_URL` | URL-и асосии API-и хидмати Giga Maps, ки барои санҷиши ҳаққонияти истифода мешавад |
| `DAILY_CHECK_APP_API_CODE` | Рамзи API барои барномаи Daily Check App, ки ҳангоми муроҷиат ба API-и хидмати Giga Maps истифода мешавад. Қиммати ҷойивазкунанда `DAILY_CHECK_APP` мебошад |
| `PCDC_APP_DOWNLOAD_URL` | URL-и боргирии версияи охирини барномаи Windows |
| `SENTRY_DSN` | (Ихтиёрӣ) DSN-и Sentry барои пайгирии хатогиҳо |

{% hint style="info" %}
`PROJECT_CONNECT_SERVICE_URL` ва `DAILY_CHECK_APP_API_CODE` танҳо дар сурате лозиманд, ки агар хоҳед аутентификатсияи дарунсохти Giga Meter-ро истифода баред (`USE_AUTH="true"`).
{% endhint %}

Намунаи пурраи `.env`:

```
DATABASE_URL="postgresql://username:password@localhost:5432/pcdc?schema=public"
USE_AUTH="true"
PROJECT_CONNECT_SERVICE_URL="https://your-giga-maps-service-url"
DAILY_CHECK_APP_API_CODE="DAILY_CHECK_APP"
PCDC_APP_DOWNLOAD_URL="https://your-windows-app-download-url"
SENTRY_DSN="your-sentry-dsn"
```

***

### Қадами 3 — Танзими пойгоҳи додаҳо

Пас аз танзими `DATABASE_URL`, мизоҷи Prisma-ро эҷод кунед. Ин фармонро **дар дохили ҷузвдони `src/prisma`** иҷро кунед:

```bash
npx prisma generate
```

***

### Қадами 4 — Иҷрои муҳоҷирати пойгоҳи додаҳо

Тағйироти зарурӣ ба `prisma.schema` (ки дар дохили `src/prisma` ҷойгир аст) ворид кунед, сипас муҳоҷиратро иҷро намоед. Ин фармонро **дар дохили ҷузвдони `src/prisma`** иҷро кунед:

```bash
npx prisma migrate dev
```

***

### Қадами 5 — Оғози сервер

Аз решаи лоиҳа:

```bash
npm run start
```

Барнома дар суроғаи `http://localhost:3000/` кор мекунад. Swagger UI дар `/api` дастрас аст. Барои дидани рӯйхати ҳамаи масирҳои API, ба `/api/all` гузаред.

***

### Аутентификатсия

Барои фаъол кардани аутентификатсия, дар файли `.env`-и худ `USE_AUTH="true"`-ро гузоред:

```
USE_AUTH="true"
```

Аутентификатсияи пешфарз дархостҳоро тавассути API-и хидмати Giga Maps бо истифода аз калиди API-и эҷодшуда санҷиш мекунад. Татбиқи он дар [`auth.guard.ts`](https://github.com/unicef/giga-meter-backend/blob/58861714ffa21c4eff1ca8ec5e629aba16594dec/src/auth/auth.guard.ts#L15) ҷойгир аст.

Барои истифодаи аутентификатсияи фармоишӣ — масалан, барои ҳамгироӣ бо низоми ҳувиятшиносии ҳукуматӣ — мантиқи `auth.guard.ts`-ро навсозӣ кунед. Барои намунаҳои татбиқ ба [ҳуҷҷатгузории аутентификатсияи NestJS](https://docs.nestjs.com/security/authentication#implementing-the-authentication-guard) нигаред.

***

→ [Насби Docker](docker.md) — ҷойгиркунии алтернативӣ бо истифодаи Docker\
→ [Талаботи инфрасохтор](infra-requirements.md) — хусусиятҳои сервер\
→ [Санҷиши воҳид](unit-testing.md) — санҷидани танзимоти Шумо пеш аз ба кор андохтан
