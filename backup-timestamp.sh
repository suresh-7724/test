#!/bin/bash
SOURCE="/home/user/Documents/web/test"
DESTINATION="/backup"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
mkdir -p "$DESTINATION/$DATE"
cp -r "$SOURCE" "$DESTINATION/$DATE"
echo "Backup completed on $DATE"
