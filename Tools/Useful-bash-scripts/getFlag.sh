#!/bin/bash

flag=$1
path=$2

found_flag=$(grep -oI "\S*$flag\S*" $path)

if [ -n "$found_flag" ]; then
  echo "The flag was found: $found_flag"
else
  echo "The flag was not found."
fi