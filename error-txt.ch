#!/bin/bash
report_file="error_report.txt"
> $report_file

find . -type f -name "*.txt" | while read file; do
  count=$(grep -i "error" "$file" | wc -l)
  echo "$file: $count" >> $report_file
done

