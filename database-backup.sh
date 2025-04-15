#!/bin/bash
read -sp "Enter database password: " DB_PASS
DB_NAME="school"
BACKUP_DIR="/backups"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
mkdir -p "$BACKUP_DIR"
mysqldump -u root -p"$DB_PASS" "$DB_NAME" > "$BACKUP_DIR/$DB_NAME-$DATE.sql"
echo -e "\nDatabase backup completed: $BACKUP_DIR/$DB_NAME-$DATE.sql"
