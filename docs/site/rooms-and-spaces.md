# Chats, rooms, and Spaces

BMatrix can start a direct chat, create an encrypted private group, create a
public room, or create a private Space. The current room-creation flow accepts
Matrix user IDs and can search the homeserver's user directory when available.

## Start or join a conversation

- To create a direct chat or group, search for a user or enter their full Matrix
  ID, such as `@alex:example.org`.
- To invite someone to a room you have opened, use the room's invite action and
  enter their full Matrix ID. The server applies the room's invitation and
  permission rules.
- To show a room QR code, open the room's invite action and choose **Show room
  QR code**. Scanning it opens the room's `matrix.to` link; it does not grant
  access to a private room.
- To join an existing room, enter its room ID, public alias, or HTTPS
  `matrix.to` link.
- To scan a room QR code, choose **Scan a room QR code** in the join dialog.
  BMatrix fills in the scanned value; review it and choose **Join a room** to
  continue. Scanning uses Google Play services and does not request camera
  permission from BMatrix. If the scanner is unavailable, enter the room ID or
  link manually.
- Share a room link from the room's share action. A link does not grant access
  to a private or invite-only room.

## Spaces

Joined Spaces appear separately from joined rooms. Creating a Space and listing
it are implemented; browsing nested Space hierarchies, adding/removing child
rooms, public aliases, and detailed administration controls are still pending.

Room creation, user search, invitations, joins, and link handling still require
validation on the target Synapse server. Public and encrypted-room options have
different visibility and encryption properties; review the choices in the app
before creating a room.
