# Conversations and files

The development preview contains a Matrix timeline and basic text composer.
Behavior described here is not yet accepted against a live homeserver or across
physical devices.

## Messages

- Send text and reply to a remote message.
- Add or remove a thumbs-up reaction; existing reactions are displayed.
- Edit or redact your own remote message. Redaction cannot remove copies that
  another member has already seen or saved.
- Forward text to a joined room. Forwarding creates a new message and identifies
  the original sender.
- Search text and attachment names in the history currently loaded in the
  conversation. Load older messages before searching older history.
- See unread counts, mark a room unread, and see typing indicators when the
  homeserver supports them.

## Attachments

Choose multiple files from Android's document picker to send them one at a
time. A later upload can fail after earlier files have already been sent.
You can also share text or content files from another Android app through its
Share action. BMatrix asks you to choose a joined conversation, opens it, and
sends the shared text and files there. The app needs access to the shared file
until the upload finishes.
Received files can be saved through Android's document picker. The conversation
gallery lists attachments in the loaded timeline; load older history to reveal
older attachments.

Forwarding an attachment downloads and decrypts it locally before sending a
new copy to the destination room. The destination copy is encrypted according
to that room's Matrix settings. Everyone who can access the destination room may
be able to read it.

Camera capture, voice messages, inline previews, cancellation/resume, and
complete history indexing are not ready.
