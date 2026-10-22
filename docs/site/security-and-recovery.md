# Security and recovery

## Keep account recovery separate from this device

Matrix end-to-end encryption keys determine whether encrypted history can be
read. Keep a verified account recovery method in a secure place and test it
before relying on BMatrix for important conversations. Never send recovery
keys, passwords, or a key-export file to support or include them in a bug report.

Importing the password-protected room-key file exported by Element Classic is
not implemented yet. The app's encrypted local session storage alone does not
restore the keys from another client or device.

## App lock and local data

An optional app lock can use Android biometrics or the device's screen-lock
credential. Choose immediate locking, one minute, or five minutes after leaving
the app. The task-switcher preview is hidden as soon as BMatrix leaves the
screen, including during a grace period. Device behavior still needs validation.

Signing out removes the local Matrix session, encrypted database, cache, and
database key after asking for confirmation. Do not sign out or uninstall while
you still need data on this device unless you have confirmed that your Matrix
account recovery can restore the encrypted history.

## Reporting a problem

Before sharing diagnostics, remove passwords, access tokens, room contents,
user IDs, homeserver-specific private details, and encryption material. Attach
only the app version and a concise description of the steps that failed.
