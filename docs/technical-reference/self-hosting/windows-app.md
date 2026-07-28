# Windows App Setup

This is an optional step for building and distributing your own version of the Giga Meter Windows app, pointed at your self-hosted backend and branded for your deployment.

{% hint style="info" %}
If you are using the standard Giga-distributed installer from [meter.giga.global](https://meter.giga.global/), skip this page.
{% endhint %}

The source repository is [unicef/project-connect-daily-check-app](https://github.com/unicef/project-connect-daily-check-app). It is built with Angular, Ionic, Capacitor, and Electron.

***

### Requirements

* A device running Windows 7 or higher — ideally one permanently and exclusively connected to the school's internet connection
* Node.js installed on the build machine

***

### Step 1 — Install dependencies

After cloning the repository:

```bash
npm install
```

***

### Step 2 — Configure branding

All branding settings live in `src/environments/environment.ts`. Set these before building.

**App name**

```typescript
appName: 'Giga Meter'
```

**App name suffix** (optional — appears in blue in the header)

```typescript
appNameSuffix: 'Daily Check'
```

**Home screen description**

Update the `title2` property in the `home` object inside each language file (`en.json`, `fr.json`, `es.json`, etc.).

**About menu**

```typescript
showAboutMenu: false  // hide the menu item
showAboutMenu: true   // show it; customise content in app.component.html (menuId="fourth")
```

***

### Step 3 — Create the build

For development:

```bash
ionic build
```

For production:

```bash
ionic build --prod
```

***

### Step 4 — Transfer the build to Electron

```bash
npx cap sync @capacitor-community/electron
```

***

### Step 5 — Navigate to the Electron folder

```bash
cd .\electron\
```

***

### Step 6 — Create the Windows installer

```bash
npm run electron:make
```

The output (`.exe` or `.msi`) is generated in `/electron/dist/`.

***

### Testing without building

To run the app in a browser during development:

```bash
ionic serve
```

To run the desktop app without generating an installer:

```bash
npm run electron:start-live
```

***

→ [Backend Installation](installation.md) — set up the backend first\
→ [Unit Testing](unit-testing.md) — validate the full setup
