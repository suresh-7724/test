#!/bin/bash
read -p "Enter Hostname or IP: " host
filename="ping_status.log"
log_file="/home/$USER/$filename"
timestamp=$(date "+%Y-%m-%d %H:%M:%S")

if ping -c 1 $host &> /dev/null; then
  echo "$timestamp SUCCESS: $host is reachable" >> $log_file
else
  echo "$timestamp FAILURE: $host is not reachable" >> $log_file
fi
