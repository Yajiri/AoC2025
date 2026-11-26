$ErrorActionPreference = "Stop"

Get-ChildItem python -Directory |
    Where-Object { Test-Path "$($_.FullName)/test_solution.py" } |
    ForEach-Object {
        Write-Host "Running tests in $($_.Name)"
        python -m unittest discover -s $_.FullName -v
    }