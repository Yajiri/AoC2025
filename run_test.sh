#!/bin/bash
set -e

python -m unittest discover -s test_*.py -v
