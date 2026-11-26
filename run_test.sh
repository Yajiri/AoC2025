#!/bin/bash
set -e

python -m unittest discover -s python/day* -p test_*.py -v
