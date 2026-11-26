# 🎄🎄 Advent of Code 2025 🎄🎄
This repo contains a consistent python environment using dockers with my solutions for the 2025 Advent of Code problems.  
🚧🚧currently only part 1 but will eventually be part 2 as well🚧🚧  
In addition to this it also contains both a bash and powershell script that will build and run said solutions in the python environment.

## 🟢 Getting started 🟢
You only need to run the git clone on this repository in order to use it.

## 🟢 Running locally 🟢
Docker is the only thing that you are required to have on your PC in order to run the code files that are in the repository.  
If you have python installed and updated to v.3+ then you can also run it the usual way on Linux:  
```python3 ./filename.py```   
or on windows:  
```python3 .\filename.py```  
  

## 👍 Docker 👍
So the docker used here is very simple and only ensures that the files can be run within a python environment.  
You can manually run these using:  
docker build -t python-env  
And then do the:  
docker run --rm \  
With the follow up commands but this is all in the scrips that will automate the process.

## ㊗️ Script ㊗️
There are two scripts first is bash which is used in GitHub Actions and Linux systems, the second one is a PowerShell script that does the same but runs on Windows systems.  
The scripts will build the docker environment if it does not already exist and then run the specified files inside of said environment. 

The commando to run the scripts are 
For bash:  
build.sh     
```./build.sh dayX/solution.py```  
X can be any day 1-12, and if you want to run the tests on the code instead of getting the answer then change solution.py to test_solution.py

You can also run:  
```./build.sh```    
This will run the day1/solution.py as I set that for standard if nothing else is specified. 

There is also a script to run the tests localy  
```./run_tests.sh```  
This will run the tests on every single excercise

For PowerShell:  
```.\build.ps1 dayX/solution.py```    
X can be any day 1-12, and if you want to run the tests on the code instead of getting the answer then change solution.py to test_solution.py

You can also just run:  
```.\build.ps1```    
This will run the day1/solution.py as I set that for standard if nothing else is specified. 

There is also a script to run the tests localy  
```./run_tests.ps1```  
This will run the tests on every single excercise

## :warning: *You might get this when trying to run PowerShell* :warning:  
Cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_policies at https:/go.microsoft.com/fwlink/?LinkID=135170.  
If this happens try running:  
```Get-ExecutionPolicy```    
It should return something similar to:  
Restricted  
The solution is to run:  
```Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass```    
