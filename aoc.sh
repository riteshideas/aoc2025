#!/bin/bash
# Usage: ./aoc.sh DAY PART
# Example: ./aoc.sh 2 1   (This runs day02p1.py for Day 2, Part 1)

# Ensure two arguments are provided: DAY and PART
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 DAY PART [--profile]"
    exit 1
fi

YEAR="2025"
DAY="$1"
PART="$2"
PROFILE=false

# Check for --profile flag
if [ "$#" -eq 3 ] && [ "$3" == "--profile" ]; then
    PROFILE=true
fi

# Set your Advent of Code session cookie here.
SESSION_COOKIE="$AdventOfCode"

# Construct the URL for the puzzle input.
INPUT_URL="https://adventofcode.com/${YEAR}/day/${DAY}/input"

echo "Downloading input for Day ${DAY} of ${YEAR} from ${INPUT_URL}..."

# Download the input without modifying it.
curl -s --cookie "session=${SESSION_COOKIE}" "$INPUT_URL" -o input.txt
truncate -s -1 input.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to download input."
    exit 1
fi

echo "Input successfully downloaded to input.txt."

# Format the day number to two digits (e.g., "2" becomes "02").
DAY_PADDED=$(printf "%02d" "$DAY")

# Construct the Python script name based on the day and part.
PYTHON_SCRIPT="day${DAY_PADDED}p${PART}.py"

# Check if the solution script exists.
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: Python script ${PYTHON_SCRIPT} not found!"
    exit 1
fi

echo "Running solution script: ${PYTHON_SCRIPT}"

if [ "$PROFILE" = true ]; then
    echo "Profiling enabled - generating flame graph..."
    PROFILE_OUTPUT="profile_day${DAY_PADDED}p${PART}.svg"
    time py-spy record -o "profiles/$PROFILE_OUTPUT" -r 1000 -- python3 "$PYTHON_SCRIPT" input.txt
        # time py-spy record -o "$profiles/{PROFILE_BASE}.speedscope.json" -f speedscope -- python3 "$PYTHON_SCRIPT" input.txt

    echo "Profile saved to ${PROFILE_OUTPUT}"
    echo "Open it in your browser to view the flame graph!"
else
    time python3 "$PYTHON_SCRIPT" input.txt
fi
