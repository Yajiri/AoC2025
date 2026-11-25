param(
    [string]$Script = "day1/solution.py"
)

$image = docker images -q python-env

if ($image) {
    Write-Host "Build already exists"
}

if (-not $image) {
    Write-Host "Building python-env..."
    docker build -t python-env .
}

docker run --rm `
  -v "${PWD}:/workspace" `
  -w /workspace `
  python-env `
  python python/$Script