# Насбкунии барномаи Windows

Ин як қадами ихтиёрист барои сохтан ва паҳн кардани нусхаи худии барномаи Giga Meter барои Windows, ки ба бэкенди худмизбонии Шумо пайваст ва барои интишори Шумо бренд карда шудааст.

{% hint style="info" %}
Агар Шумо насбкунандаи стандартии аз ҷониби Giga паҳншударо аз [meter.giga.global](https://meter.giga.global/) истифода баред, ин саҳифаро гузаред.
{% endhint %}

Анбори манбаъ [unicef/project-connect-daily-check-app](https://github.com/unicef/project-connect-daily-check-app) мебошад. Он бо Angular, Ionic, Capacitor ва Electron сохта шудааст.

***

### Талабот

* Дастгоҳе, ки Windows 10 ё болотар дорад — беҳтараш дастгоҳе, ки доимӣ ва танҳо ба пайвастшавии интернети мактаб пайваст аст
* Node.js дар мошини сохтан насб шуда бошад

***

### Қадами 1 — Насб кардани вобастагиҳо

Пас аз клон кардани анбор:

```bash
npm install
```

***

### Қадами 2 — Танзими бренд

Ҳамаи танзимоти бренд дар файли `src/environments/environment.ts` ҷойгиранд. Пеш аз сохтан онҳоро танзим кунед.

**Номи барнома**

```typescript
appName: 'Giga Meter'
```

**Пасванди номи барнома** (ихтиёрӣ — бо ранги кабуд дар сарлавҳа намоён мешавад)

```typescript
appNameSuffix: 'Daily Check'
```

**Тавсифи саҳифаи асосӣ**

Хосияти `title2`-ро дар объекти `home`, ки дар ҳар як файли забон (`en.json`, `fr.json`, `es.json` ва ғайра) ҷойгир аст, навсозӣ кунед.

**Менюи «Дар бораи барнома»**

```typescript
showAboutMenu: false  // пинҳон кардани ин банди меню
showAboutMenu: true   // намоиш додани он; мазмунро дар app.component.html (menuId="fourth") созед
```

***

### Қадами 3 — Сохтани build

Барои таҳия:

```bash
ionic build
```

Барои истеҳсолот:

```bash
ionic build --prod
```

***

### Қадами 4 — Интиқоли build ба Electron

```bash
npx cap sync @capacitor-community/electron
```

***

### Қадами 5 — Гузаштан ба папкаи Electron

```bash
cd .\electron\
```

***

### Қадами 6 — Сохтани насбкунандаи Windows

```bash
npm run electron:make
```

Натиҷа (`.exe` ё `.msi`) дар `/electron/dist/` эҷод мешавад.

***

### Санҷиш бидуни сохтан

Барои иҷрои барнома дар браузер ҳангоми таҳия:

```bash
ionic serve
```

Барои иҷрои барномаи мизи корӣ бидуни эҷоди насбкунанда:

```bash
npm run electron:start-live
```

***

→ [Насбкунии бэкенд](installation.md) — аввал бэкендро насб кунед\
→ [Санҷиши воҳид](unit-testing.md) — насбкунии пурраро тасдиқ кунед
