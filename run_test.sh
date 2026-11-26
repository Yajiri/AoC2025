#!/bin/bash
set -e

python -m unittest discover -s python -p test_*.py -v
