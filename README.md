<h1 align="center"> 🎄🎄 Advent of Code 2025 🎄🎄</h1>
This repo contains a consistent python environment using dockers with my solutions for the 2025 Advent of Code problems.<br>  
🚧🚧currently only part 1 but will eventually be part 2 as well🚧🚧<br>  
In addition to this it also contains both a bash and powershell script that will build and run said solutions in the python environment.

<h2> 🟢 Getting started 🟢</h2>
You only need to run the git clone on this repository in order to use it.

<h2> 🟢 Running locally 🟢</h2>
Docker is the only thing that you are required to have on your PC in order to run the code files that are in the repository.<br>  
If you have python installed and updated to v.3+ then you can also run on <br>   
Linux:  <br>
```python3 ./filename.py``` <br>   
Windows:  <br>
```python3 .\filename.py```  <br>
  

<h2> 👍 Docker 👍</h2>
So the docker used here is very simple and only ensures that the files can be run within a python environment.<br>
You can manually run these using:<br>
```docker build -t python-env```<br>
And then do the in Linux:<br>
```docker run --rm \```<br>
or Windows:<br>  
```docker run --rm ` ```<br>  
With the follow up commands but this is all in the scrips that will automate the process.<br>

<h2> ㊗️ Script ㊗️</h2>
There are two scripts first is bash which is used in GitHub Actions and Linux systems, the second one is a PowerShell script that does the same but runs on Windows systems.<br>  
The scripts will build the docker environment if it does not already exist and then run the specified files inside of said environment.<br> 

The commando to run the scripts are<br> 
For bash:<br>  
build.sh<br>     
```./build.sh dayX/solution.py```<br>  
X can be any day 1-12, and if you want to run the tests on the code instead of getting the answer then change solution.py to test_solution.py<br>

You can also run:<br>  
```./build.sh```<br>    
This will run the day1/solution.py as I set that for standard if nothing else is specified.<br> 

There is also a script to run the tests localy<br>  
```./run_tests.sh```<br>  
This will run the tests on every single excercise<br>

For PowerShell:<br>  
```.\build.ps1 dayX/solution.py```<br>    
X can be any day 1-12, and if you want to run the tests on the code instead of getting the answer then change solution.py to test_solution.py<br>

You can also just run:<br>  
```.\build.ps1```<br>   
This will run the day1/solution.py as I set that for standard if nothing else is specified.<br> 

There is also a script to run the tests localy<br>  
```./run_tests.ps1```<br>  
This will run the tests on every single excercise<br>

<h2><i> :warning: You might get this when trying to run PowerShell :warning: </i></h2>
Cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_policies at https:/go.microsoft.com/fwlink/?LinkID=135170.<br> 

If this happens try running:<br>    
```Get-ExecutionPolicy```<br>  

It should return something similar to:<br>     
```Restricted```<br>  

The solution is to run:<br>  
```Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass```  
