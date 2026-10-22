# Project status

This preview describes development code, not a supported production release.
The latest Android debug build and lint passed in GitHub Actions for source
commit `47b53a3`. Sign-in, encryption, messaging, attachments, QR scanning, and
room operations have not yet been validated on devices against the maintainer's
live Synapse homeserver.

The app source currently contains a sign-in flow, encrypted local session
storage, Matrix synchronization, text messaging, replies, reactions, editing,
redaction, text and file forwarding, file transfer, multi-file selection, receiving
Android Sharesheet text and files, a loaded-history file gallery, room/Space
creation, invitations, sharing room permalinks, and joining a room by ID, alias, or
`matrix.to` link. The current source can also display a room-link QR code and
scan one into the join dialog. The join dialog asks the user to continue; a QR
code does not grant access to a private room. The scanner uses Google Play
services and does not request camera permission from BMatrix. A successful build
does not confirm that these features work with a specific server, account,
encrypted room, or Android device.

Wide tablet layouts display the joined room/Space list alongside the active
conversation. This layout has not yet been checked on a physical tablet.

Voice/video calls, group calls, screen sharing, incoming-call notifications,
Element Classic key-file import, voice messages,
full-history media search, and a supported signed release are not ready. An
update-check/download flow is implemented, but no public signed release exists
for it to install or validate yet. This documentation is a
pre-release preview, not an acceptance statement. Android may open an incoming
`matrix.to` link in BMatrix; opening the link does not bypass room visibility or
invitation permissions.

The supported guide will identify its app version and provide verified
installation, sign-in, recovery, rooms, calls, screen-sharing, security,
updates, and troubleshooting instructions. The current preview documents only
behavior present in the source and marks features that still need validation.
