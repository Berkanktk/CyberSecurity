# IMAP Commands
IMAP allows synchronizing read, moved, and deleted messages. IMAP is quite convenient when you check your email via multiple clients. Unlike POP3, which tends to minimize server storage as email is downloaded and deleted from the remote server, IMAP tends to use more storage as email is kept on the server and synchronized across the email clients.

| Command | Description | Example |
|---|---| --- |
| CAPABILITY | Requests a list of capabilities supported by the server | CAPABILITY |
| LOGIN | Authenticates the user and logs in to the mailbox | LOGIN username password |
| LOGOUT | Closes the connection to the server and logs out of the mailbox | LOGOUT |
| SELECT | Selects a mailbox to access | SELECT INBOX |
| EXAMINE | Selects a mailbox to access in read-only mode | EXAMINE INBOX |
| CREATE | Creates a new mailbox | CREATE mailbox |
| DELETE | Deletes an existing mailbox | DELETE mailbox |
| RENAME | Renames an existing mailbox | RENAME oldmailbox newmailbox |
| SUBSCRIBE | Subscribes to a mailbox | SUBSCRIBE mailbox |
| UNSUBSCRIBE | Unsubscribes from a mailbox | UNSUBSCRIBE mailbox |
| LIST | Lists mailboxes | LIST "" "*" |
| LSUB | Lists subscribed mailboxes | LSUB "" "*" |
| STATUS | Requests status information for a mailbox | STATUS mailbox (MESSAGES) |
| APPEND | Appends a message to a mailbox | APPEND mailbox flags date-time message |
| CHECK | Requests a checkpoint of the currently selected mailbox | CHECK |
| CLOSE | Closes the currently selected mailbox | CLOSE |
| EXPUNGE | Permanently removes messages marked for deletion in the currently selected mailbox | EXPUNGE | 
| SEARCH | Searches for messages in the currently selected mailbox | SEARCH charset criteria |
| FETCH | Retrieves data for messages in the currently selected mailbox | FETCH sequence data-items |
| STORE | Alters flags for messages in the currently selected mailbox | STORE sequence data-items | 
| COPY | Copies messages from the currently selected mailbox to another mailbox | COPY sequence mailbox |
| UID | Issues commands that refer to messages by their unique identifier (UID) instead of their message sequence number | UID command |

Sequence numbers are used to identify messages in IMAP. They are assigned by the server and are unique to the mailbox. The UID command is used to refer to messages by their unique identifier instead of their sequence number.

Data items are used to specify what data to retrieve or alter in a message. They can include message flags, message headers, message body, and more.