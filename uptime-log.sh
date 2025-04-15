#!/bin/bash
LOG_FILE="system_uptime.log"
echo "$(date): $(uptime -p)" >> $LOG_FILE
