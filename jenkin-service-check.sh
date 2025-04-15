#!/bin/bash
SERVICE="jenkins"
if systemctl is-active --quiet $SERVICE; then
  echo "$SERVICE is running"
else
  echo "$SERVICE is not running, starting now..."
  sudo systemctl start $SERVICE
  echo "$SERVICE has been started."
fi
