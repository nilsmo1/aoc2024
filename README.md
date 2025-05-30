# --- Advent of code 2024! ---
These are my solutions to [Advent of Code 2024](https://adventofcode.com/2024).
***
## Format
The days are split up into separate folders, where each folder contains:
| Filename | Description |
| :--- | :--- |
| __main.py__ | A file with the solutions to the problems, written in Python 3.12.6. |
| __sample__ | A file with that day's sample input. This is used for some simple tests. |
| __puzzle-input__ | A file with my unique puzzle input that day. |

## Download and usage
```bash
$ git clone git@github.com:nilsmo1/aoc2024.git
$ cd aoc2024/
```
To use this repo as I intended, you should only need `curl` and some version of `python3`. If you don't want to use the __NEWDAY.sh__, you only need `python3`.

## Code template
I've included a template which I use for my code to have a consistent structure of each day's solution.

## Script for starting a new day 
The file **NEWDAY.sh** is a template script which takes in the number of a day and creates a folder for that day. It creates the needed files and uses `curl` to download that day's puzzle input into the __puzzle-input__ file. 
To use this script you need to replace the "__?__" in:
```sh
curl -o puzzle-input -b 'session=?' https://adventofcode.com/2024/day/$1/input
```
With the value of your own session cookie (which can usually be found when inspecting the Advent of Code website after loggin in).
This script only needs to run once per day, and should therefore not cause any traffic issues.
