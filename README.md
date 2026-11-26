<h1 align="center" color=red> 🎄🎄 Advent of Code 2025 🎄🎄</h1>
This repo contains a consistent python environment using dockers with my solutions for the 2025 Advent of Code problems.<br>  
🚧🚧currently only part 1 but will eventually be part 2 as well🚧🚧<br>  
In addition to this it also contains both a bash and powershell script that will build and run said solutions in the python environment.

<h2> 🟢 Getting started 🟢</h2>
You only need to run the git clone on this repository in order to use it.

<h2> 🟢 Running locally 🟢</h2>
Docker is the only thing that you are required to have on your PC in order to run the code files that are in the repository.<br>  
If you have python installed and updated to v.3+ then you can also run on <br>   
Linux:  <br>
<pre><code>python3 ./filename.py</code></pre>  
Windows:  <br>
<pre><code>python3 .\filename.py</code></pre>
  

<h2> 👍 Docker 👍</h2>
So the docker used here is very simple and only ensures that the files can be run within a python environment.<br>
You can manually run these using:<br>
<pre><code>docker build -t python-env</code></pre>
And then do the in Linux:<br>
<pre><code>docker run --rm \</code></pre>
or Windows:<br>  
<pre><code>docker run --rm ` </code></pre>  
With the follow up commands but this is all in the scrips that will automate the process.<br>

<h2> ㊗️ Script ㊗️</h2>
There are two scripts first is bash which is used in GitHub Actions and Linux systems, the second one is a PowerShell script that does the same but runs on Windows systems.<br>  
The scripts will build the docker environment if it does not already exist and then run the specified files inside of said environment.<br> 

The commando to run the docker building and code running scripts are<br> 
For bash:       
<pre><code>./build.sh dayX/solution.py</code></pre>  
X can be any day 1-12, and if you want to run the tests on the code instead of getting the answer then change solution.py to test_solution.py<br>

You can also run:  
<pre><code>./build.sh</code></pre>   
This will run the day1/solution.py as I set that for standard if nothing else is specified.<br> 

There is also a script to run the tests localy:  
<pre><code>./run_tests.sh</code></pre> 
This will run the tests on every single excercise<br>

For PowerShell:  
<pre><code>.\build.ps1 dayX/solution.py</code></pre>    
X can be any day 1-12, and if you want to run the tests on the code instead of getting the answer then change solution.py to test_solution.py<br>

You can also just run: 
<pre><code>.\build.ps1</code></pre>  
This will run the day1/solution.py as I set that for standard if nothing else is specified.<br> 

There is also a script to run the tests localy: 
<pre><code>./run_tests.ps1</code></pre>  
This will run the tests on every single excercise<br>

<h2><i> :warning: You might get this when trying to run PowerShell :warning: </i></h2>
Cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_policies at https:/go.microsoft.com/fwlink/?LinkID=135170.<br> 

If this happens try running:   
<pre><code>Get-ExecutionPolicy</code></pre>  

It should return something similar to:    
<pre><code>Restricted</code></pre>  

The solution is to run: 
<pre><code>Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass</code></pre>  
