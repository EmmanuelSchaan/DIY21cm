#!/bin/bash

# Get the directory where this script resides
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create a log subdirectory inside that location
log_dir="$script_dir/log"
mkdir -p "$log_dir"

# Generate timestamp: YYYYMMDD_HHMMSS (all two-digit padded)
timestamp=$(date +"%Y%m%d_%H%M%S")

# Define log file path
logfile="$log_dir/log_exposure_$timestamp.txt"

# Run the 21 cm capture script in the background and log output
nohup "$script_dir/ekos_exposure_on.py" > "$logfile" 2>&1 &
