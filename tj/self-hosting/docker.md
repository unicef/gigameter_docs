# Танзими Docker

Docker роҳи алтернативӣ барои иҷрои backend-и Giga Meter аст, бидуни насб кардани Node.js ва PostgreSQL мустақиман дар хост.

{% hint style="warning" %}
Танзими Docker барои Giga Meter аз ҷониби ҷомеа таҳия шудааст ва аз тарафи Giga **расман дастгирӣ намешавад**. Giga ислоҳи хатоҳо ва беҳтаркунии ҳуҷҷатҳоро қабул мекунад, аммо мутобиқат ё дастгирии татбиқҳои дар асоси Docker сохташударо кафолат намедиҳад. Истифодаро бо масъулияти худи Шумо анҷом диҳед.
{% endhint %}

***

### Талаботи пешакӣ

* Docker дар хост насб шудааст
* Docker Compose (`docker compose` бе тире — стандарти ҷорие, ки Docker расман тавсия медиҳад)

***

### Сохтани тасвир

[Dockerfile](https://github.com/unicef/giga-meter-backend/blob/58861714ffa21c4eff1ca8ec5e629aba16594dec/Dockerfile) дар анбор мавҷуд аст. Онро бо фармони зерин созед:

```bash
docker build -f Dockerfile -t repo:tag .
```

`repo:tag`-ро бо номи тасвир ва тег (tag)-и дилхоҳи Шумо иваз кунед.

***

### Иҷрои контейнер

Барнома дар порт 3000 кор мекунад. Тағйирёбандаҳои муҳити атроф (environment variables)-ро бо флагҳои `-e` интиқол диҳед:

```bash
docker run -d -p 3000:3000 \
  -e DATABASE_URL="postgresql://username:password@localhost:5432/pcdc?schema=public" \
  -e DAILY_CHECK_APP_API_CODE="DAILY_CHECK_APP" \
  -e USE_AUTH="true" \
  -e PROJECT_CONNECT_SERVICE_URL="https://your-giga-maps-service-url" \
  -e PCDC_APP_DOWNLOAD_URL="https://your-windows-app-download-url" \
  repo:tag
```

Флаги `-d` контейнерро дар паснамо иҷро мекунад. Backend дар суроғаи `http://localhost:3000/` дастрас хоҳад буд. Барои тавзеҳи ҳамаи тағйирёбандаҳои муҳити атроф ба [Насбкунии Backend](installation.md) нигаред.

***

→ [Насбкунии Backend](installation.md) — насбкунии стандартӣ (бе Docker)\
→ [Санҷиши воҳид](unit-testing.md) — тасдиқи ҷойгиркунӣ
