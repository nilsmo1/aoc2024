#!/usr/bin/env bash
xdg-open "https://adventofcode.com/2024/day/$1" > /dev/null 2>&1
dir=$(printf "day%02d" $1)
mkdir $dir
touch $dir/sample
echo "# Day $1
$(cat template)" > $dir/main.py
curl -o $dir/puzzle-input -b 'session=?' https://adventofcode.com/2024/day/$1/input
