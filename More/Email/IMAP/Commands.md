# IMAP Commands
| Command | Description |
|---|---|
| CAPABILITY | Requests a list of capabilities supported by the server |
| LOGIN | Authenticates the user and logs in to the mailbox |
| LOGOUT | Closes the connection to the server and logs out of the mailbox |
| SELECT | Selects a mailbox to access |
| EXAMINE | Selects a mailbox to access in read-only mode |
| CREATE | Creates a new mailbox |
| DELETE | Deletes an existing mailbox |
| RENAME | Renames an existing mailbox |
| SUBSCRIBE | Subscribes to a mailbox |
| UNSUBSCRIBE | Unsubscribes from a mailbox |
| LIST | Lists mailboxes |
| LSUB | Lists subscribed mailboxes |
| STATUS | Requests status information for a mailbox |
| APPEND | Appends a message to a mailbox |
| CHECK | Requests a checkpoint of the currently selected mailbox |
| CLOSE | Closes the currently selected mailbox |
| EXPUNGE | Permanently removes messages marked for deletion in the currently selected mailbox |
| SEARCH | Searches for messages in the currently selected mailbox |
| FETCH | Retrieves data for messages in the currently selected mailbox |
| STORE | Alters flags for messages in the currently selected mailbox |
| COPY | Copies messages from the currently selected mailbox to another mailbox |
| UID | Issues commands that refer to messages by their unique identifier (UID) instead of their message sequence number |