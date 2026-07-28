# Windows App Setup

This is an optional step for configuring and distributing your own version of the Giga Meter Windows app with your self-hosted backend and custom branding.

{% hint style="info" %}
If you are using the standard Giga-distributed installer from [meter.giga.global](https://meter.giga.global/), skip this page.
{% endhint %}

The source repository is [unicef/project-connect-daily-check-app](https://github.com/unicef/project-connect-daily-check-app).

***

### Getting started

Full setup and deployment instructions are in the [repository README](https://github.com/unicef/project-connect-daily-check-app/tree/prod?tab=readme-ov-file#deploying-the-daily-check-app). The steps below cover branding configuration only.

***

### Requirements

* Windows 7 or higher (the target device for installation — not the build machine)
* The device should be permanently and exclusively connected to the school's internet connection

***

### Configuration

All branding settings are in `src/environments/environment.ts`.

**App name**

Set the `appName` property. This is the name that appears in the title bar and installer.

```typescript
appName: 'Giga Meter'
```

**App name suffix**

Set the `appNameSuffix` property. This is optional — it appears in blue in the header and on the home screen, typically used to distinguish a country-specific deployment.

```typescript
appNameSuffix: 'Daily Check'
```

**Description text**

Update the `title2` property in the `home` object within each language file (`en.json`, `es.json`, `fr.json`, etc.) to change the description shown on the home screen.

**About menu**

Control the About menu item with the `showAboutMenu` property:

```typescript
showAboutMenu: false  // hide the menu item
showAboutMenu: true   // show it; customise the content in app.component.html (menuId="fourth")
```

***

→ [Backend Installation](installation.md) — set up the backend first\
→ [Unit Testing](unit-testing.md) — validate the full setup
