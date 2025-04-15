#!/bin/bash
iterations=10
count=0

while [ $count -lt $iterations ]; do
  cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
  usage=${cpu%.*}
  
  if (( usage < 10 )); then
    continue
  elif (( usage > 90 )); then
    echo "CPU usage is too high: $usage%. Exiting."
    break
  else
    echo "Iteration $((count+1)): CPU Usage: $usage%"
  fi
  ((count++))
  sleep 2
done
