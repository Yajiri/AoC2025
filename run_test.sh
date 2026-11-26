#!/bin/bash
set -e

for dir in python/day*/; do
    if [ -f "${dir}test_solution.py" ]; then
        echo "Running tests in $dir"
        python -m unittest discover -s "$dir" -v
    fi
done