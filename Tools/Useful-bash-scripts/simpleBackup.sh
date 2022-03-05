#!/bin/bash

# Backup the contents of desktop folder for current user
tar czf ~/BACKUP.tgz ~/Desktop

# Save into log
echo "$(date)" >> ~/BACKUP.log
