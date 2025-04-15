#!/bin/bash
dir="/home/suresh/Documents/web"
max_size=$((500 * 1024 * 1024))  # 500 MB in bytes
filename="dir_size_alert.log"
log_file="/home/$USER/$filename"

dir_size=$(du -sb "$dir" | cut -f1)
timestamp=$(date "+%Y-%m-%d %H:%M:%S")

if (( dir_size > max_size )); then
  echo "$timestamp WARNING: $dir exceeds 500MB with size $(du -sh "$dir" | cut -f1)" >> $log_file
fi
