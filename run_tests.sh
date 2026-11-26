#!/bin/bash
set -e

for dir in python/day*/; do
    if [ -f "${dir}test_solution.py" ]; then
        day=$(basename "$dir")

        echo "::group::Run test $day"
        python -m unittest discover -s "$dir" -v
        echo "::endgroup::"
    fi
done