#!/bin/bash
URLS=("https://example.com" "https://google.com")
for URL in "${URLS[@]}"; do
  RESPONSE_TIME=$(curl -o /dev/null -s -w '%{time_total}' $URL)
  echo "Response time for $URL: $RESPONSE_TIME seconds"
done
