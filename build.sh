#!/usr/bin/env bash
set -euo pipefail

SCRIPT="day1/solution.py"

if [$# -ge 1]; then
    SCRIPT="$1"
fi

#Check for already existing one
IMAGE=$(docker images -q python-env || true)

if [ -n "$IMAGE" ]; then
  echo "Build already exists"
else
  echo "Building python-env..."
  docker build -t python-env .
fi

# Run container
docker run --rm \
  -v "${PWD}:/workspace" \
  -w /workspace \
  python-env \
  python "python/${SCRIPT}"