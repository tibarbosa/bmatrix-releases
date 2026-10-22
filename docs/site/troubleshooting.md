# Troubleshooting

## Sign-in fails

- Confirm the homeserver URL uses `https://` and is the public Matrix base URL.
- Check the username and password with your server administrator.
- Confirm the account exists and password sign-in is enabled on the server.
- Try again on a network that can reach the server. Do not disable certificate
  validation to work around a TLS problem.

## A room or message is missing

The app currently lists joined rooms and shows the history loaded in the active
timeline. Older messages and attachments may require loading earlier history.
Private room links do not bypass invitations or room permissions.

## A file will not send or open

The homeserver and reverse proxy may enforce upload limits. Try a smaller file
and check that Android has access to the selected document. A multi-file send is
sequential, so some earlier files may have been delivered before a later item
failed.

## Calls, notifications, and key import

Voice/video calls, screen sharing, push notifications, and import of Element
Classic room-key exports are not available yet. Check the [project status](status.md)
for updates; reinstalling or changing networks will not enable these features.
