#!/bin/bash

is_prime() {
  num=$1
  if (( num <= 1 )); then
    echo "$num is not prime"
    return
  fi

  for ((i=2; i<=num/2; i++)); do
    if (( num % i == 0 )); then
      echo "$num is not prime"
      return
    fi
  done
  echo "$num is a prime number"
}

read -p "Enter a number: " number
is_prime $number
