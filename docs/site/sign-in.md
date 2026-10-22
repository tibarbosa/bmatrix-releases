# Sign in

## Requirements

Ask your Matrix administrator for an account and the public HTTPS address of
the homeserver. BMatrix does not create accounts on Synapse. Registration must
be enabled or the administrator must create the account for you.

## Steps

1. Open BMatrix and enter the homeserver address. It must start with `https://`.
   The configured default can be changed on the sign-in screen.
2. Enter your Matrix username and password, then sign in.
3. If Android asks to allow notifications, decide whether BMatrix may show
   message and call alerts. Push delivery is not available in this preview.
4. Complete any Matrix device-verification or encryption prompts shown by the
   app. The exact verification workflow is still under development.

If you change the server, use its full public base URL, not a room URL or the
Synapse container address. If sign-in fails, check the address, account status,
network access, and server TLS certificate with your administrator.

## Encrypted rooms

The client stores its Matrix session and database key in app-private encrypted
storage. This is not a replacement for setting up and testing Matrix account
recovery. Do not assume old encrypted messages are readable until the device is
verified and the relevant history has synchronized.
