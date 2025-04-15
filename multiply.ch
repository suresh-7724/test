#!/bin/bash
output_file="multiplication_table.txt"
> $output_file

for i in {1..5}; do
  echo "Multiplication Table for $i:" >> $output_file
  for j in {1..10}; do
    echo "$i x $j = $((i * j))" >> $output_file
  done
  echo "" >> $output_file
done

cat $output_file
