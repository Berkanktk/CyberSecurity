# SMTP
Simple Mail Transfer Protocol (SMTP) defines how a mail client talks with a mail server and how a mail server talks with another.

| Command | Description | Example |
|---|---|---|
| HELO [domain] | Identifies the client to the server | HELO mail.example.com |
| EHLO [domain] | Extended HELO command that requests extended features | EHLO mail.example.com |
| MAIL FROM: [email] | Specifies the sender's email address | MAIL FROM: [email] |
| RCPT TO: [email] | Specifies the recipient's email address | RCPT TO: [email] |
| DATA | Indicates the start of the email message | DATA |
| QUIT | Closes the connection | QUIT |
