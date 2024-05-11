#!/bin/bash

# Recursive function to find and delete files
delete_files() {
	local dir="$1"

	# Check if the current directory contains the target file
	if [ -f "$dir/input.txt" ]; then
		rm "$dir/input.txt"
		echo "Deleted $dir/input.txt"
	fi

	# Recursively traverse subdirectories
	for subdir in "$dir"/*; do
		if [ -d "$subdir" ]; then
			delete_files "$subdir"
		fi
	done
}

# Start from the current directory
delete_files "$(pwd)"
