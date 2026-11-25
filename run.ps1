docker build -t python-env .

docker run --rm `
  -v "${PWD}:/workspace" `
  -w /workspace `
  python-env `
  python quest1/day1.py