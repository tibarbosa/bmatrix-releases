# Install BMatrix

## Release availability

There is not yet a supported signed release. The APK produced by a local
development build is debug-signed and is not suitable for normal installation
or in-app upgrades. Wait for a version to appear on the public
[BMatrix releases page](https://github.com/tibarbosa/bmatrix-releases/releases).

When a signed release is available:

1. Open the release page and download the APK matching your device processor.
   Most recent Android phones and tablets use `arm64-v8a`.
2. Check the release notes and SHA-256 checksum published with that APK.
3. Open the downloaded APK. If Android asks, allow your browser or file manager
   to install apps from this source, then return to the installer.
4. Review Android's package installer and confirm the installation.
5. Open BMatrix and continue to [sign in](sign-in.md).

The minimum supported Android version is 10 (API 29). Phones and tablets are
both in scope; physical-device installation and tablet acceptance are still
pending.

## Update an existing installation

Install an update over the existing BMatrix app. Do not uninstall first:
uninstalling removes the local encrypted Matrix store. Android requires the new
APK to be signed by the same release key and asks you to confirm installation.
The in-app update flow is implemented, but has not yet been proven between two
published releases.

## Build a development APK

Developers can follow the private repository's setup instructions. A debug APK
is for testing only; it is not a supported end-user download and cannot update a
release-signed installation.
