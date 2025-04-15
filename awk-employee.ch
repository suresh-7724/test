#!/bin/bash

awk -F, '
NR > 1 {
  dept[$2] += $3
  count[$2]++
  
  split($4, d, "-")
  year = d[1]
  if (2024 - year > 5) {
    print "Over 5 years: " $1 " (" $4 ")"
  }
}
END {
  for (d in dept) {
    print "Average salary in " d ": " dept[d]/count[d]
  }
}' employee.csv
