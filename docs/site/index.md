# BMatrix user guide

BMatrix is a Matrix client for Android phones and tablets running Android 10 or
later. It connects to a Matrix homeserver that you choose and stores its
encrypted client data on your device.

**Guide version:** {{ app_version }} · **Documentation revision:** {{ docs_revision }}

> **Development preview:** BMatrix has no supported signed APK release yet. The
> published feature notes below describe code that is still being validated
> against real accounts and devices. Do not use a development build as the only
> copy of important encryption keys or conversation data.

## Before you begin

- You need an account on a Matrix homeserver. BMatrix does not create server
  accounts; an administrator must create one or enable registration.
- For encrypted rooms, keep a separate, secure recovery method for your Matrix
  account. BMatrix does not yet import Element Classic room-key export files.
- A public signed APK, installation steps, and tested update path are not
  available yet.

## Guides

```{toctree}
:maxdepth: 2

install
sign-in
conversations
rooms-and-spaces
security-and-recovery
updates
troubleshooting
status
```

## Current application status

The preview includes account sign-in, encrypted local session storage, room
lists, text conversations, and early room and attachment workflows. Calls,
screen sharing, push notifications, and import of Element Classic key exports
are not ready. Read [current status](status.md) before installing or relying on
any feature.
