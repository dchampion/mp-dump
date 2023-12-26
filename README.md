# Mountain Project API Consumer
## Summary
The Mountain Project API Consumer is a small Python program that retrieves data from the <a href=https://www.mountainproject.com/data target="_blank">Mountain Project REST APIs</a> and stores the results in comma-separated text (.csv) files.

## Requirements
To run this program, Python 3+ must be installed on your computer.

To check if Python is installed on your computer, and if so to verify you have version 3 or greater, open a terminal window (e.g. <code>cmd</code> in Windows or <code>bash</code> in Linux) and type <code>python --version</code> (if using <code>Terminal</code> in MacOS, type <code>python3 --version</code>).

## Install the Mountain Project API Consumer
Use one of the following methods to install the Mountain Project API Consumer on your computer:
* If Git is installed, navigate to a clean directory on your file system and type <code>git clone https<nolink>://github.com/dchampion/mp-dump.git</code>. This will install the program into a subdirectory called <code>mp-dump</code>.

* If <code>Git</code> is not installed, or you do not wish to use it, click the <code>Code</code> button on this page and select <code>Download ZIP</code> to download and extract a zipped version of the program into a clean file system directory.

## Set Up a Virtual Environment
To avoid polluting your global Python environment with the dependencies required by this program, set up and activate a virtual environment. Execute all of the following commands from a command-line prompt in the directory into which you cloned/installed the program.

* Install your virtual environment:

    * If using <code>Windows</code> (cmd) or <code>Linux</code> (bash), type <code>python -m venv .venv</code>

    * If using <code>MacOS</code> (Terminal), type <code>python3 -m venv .venv</code>

* Activate your virtual environment:

    * If using <code>Windows</code> (cmd), type <code>".venv/Scripts/activate.bat"</code> (you must include the double-quotes for this command to work).

    * If using <code>Linux</code> (bash) or <code>MacOS</code> (Terminal), type <code>source .venv/bin/activate</code> (note on some systems the path may be <code>.venv/Scripts/activate</code>).

* Install the program dependencies into your virtual environment:

    * Type <code>pip install -r requirements.txt</code>

With the successful completion of these three steps, you should be ready to consume the Mountain Project REST APIs.

## Run the Mountain Project API Consumer
Type <code>python mp_dump.py</code> to display a comprehensive help page, including examples, for using this program.

<b>IMPORTANT:</b> You will need to supply a valid Mountain Project-supplied user key to execute any and all requests supplied by this program (the key used in the examples will not work). To get your private key, go to the <a href=https://www.mountainproject.com/data>Mountain Project API page</a>, and click the link <code>Sign up or log in to get your key</code>.

A successful command will display the message <code>MPAC ran successfully</code>. The requested information will be retrieved and stored in one of four .csv files, depending on the type of information requested.

If the program encounters a failure of any kind, diagnostic information will be printed on your screen which should help you to troubleshoot the problem.