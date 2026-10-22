# Updates

The Settings screen contains an update-check and download flow. It reads the
public release manifest, chooses a build for the device ABI, downloads it to
private app storage, and checks its size, SHA-256, package ID, version, and
signer against the installed app. Android then displays the system installer;
you must allow installation from BMatrix if requested and confirm the update.

There is no public signed APK or release manifest yet, so this flow cannot
currently find an update. Its behavior across two signed releases has not been
accepted yet.

When a release is available, keep the installed app. Android only accepts an
update signed with the same app signing key. Never install an APK from an
unofficial mirror or bypass a signature, package, or checksum warning.
