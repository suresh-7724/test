#!/bin/bash
source_dir="/home/ubuntu/data"
backup_dir="/home/ubuntu/backups"
log_file="/home/userlog"
filename="backup_$(date +%Y%m%d_%H%M%S).tar.gz"

mkdir -p $backup_dir

find "$source_dir" -type f -mtime -1 | tar -czf "$backup_dir/$filename" -T - 2>> $log_file

if [ $? -eq 0 ]; then
  echo "$(date): Backup successful - $filename" >> $log_file
else
  echo "$(date): Backup failed" >> $log_file
fi
0 1 * * * /bin/bash /home/ubuntu/incremental_backup.sh
