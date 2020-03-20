# Mountain Project API Consumer
## Summary
The Mountain Project API Consumer (MPAC) is a small Python program that retrieves data from the <a href=https://www.mountainproject.com/data target="_blank">Mountain Project REST APIs</a> and stores the results in comma-separated text (.csv) files.

## Requirements
To run MPAC, Python version 3+ must be installed on your computer.

To check if Python is already installed on your computer, and if so to verify you have version 3 or greater, open a terminal window (e.g. <code>cmd</code> in Windows, <code>bash</code> in Linux, or <code>Terminal</code> in MacOS) and type <code>python --version</code>. If the version displayed is less than 3, or you receive an error, download and install the latest Python version <a href=https://www.python.org/downloads target="_blank">here</a></i>.

## Install the Mountain Project API Consumer
Use one of the following methods to install MPAC on your computer:
* If Git is installed, navigate to a clean directory on your file system and type <code>git clone https<nolink>://github.com/dchampion/mp-dump.git</code>. This will install MPAC into a subdirectory called <code>mp-dump</code>.

* Alternatively, if <code>Git</code> is not installed, or you do not wish to use it, click the <code>Clone or download</code> button on this page to download and extract a zipped version of MPAC into a clean file system directory.

## Set Up a Virtual Environment
To avoid polluting your global Python environment with the dependencies required by MPAC, set up and activate a virtual environment. Execute all of the following commands from a command-line prompt in the directory into which you cloned/installed MPAC.

* Install your virtual environment:

    * If using <code>cmd</code> (Windows) or <code>bash</code> (Linux), type <code>python -m venv .venv</code>

    * If using <code>Terminal</code> (MacOS), type <code>python3 -m venv .venv</code>

* Activate your virtual environment:

    * If using <code>cmd</code> (Windows), type <code>".venv/Scripts/activate.bat"</code> (you must include the double-quotes for this command to work).

    * If using <code>bash</code> (Linux) or <code>Terminal</code> (MacOS), type <code>source .venv/bin/activate</code>

* Install the MPAC dependencies into your virtual environment:

    * Type <code>pip install -r requirements.txt</code>

With the successful completion of these three steps, you should be ready to consume the Mountain Project REST APIs.

## Run the Mountain Project API Consumer
Type <code>python mp_dump.py</code> to display a comprehensive help page, including examples, for using MPAC.

<b>IMPORTANT:</b> You will need to supply a valid Mountain Project-supplied user key to execute any and all requests with MPAC (the key used in the examples will not work). To get your private key, go to the <a href=https://www.mountainproject.com/data>Mountain Project API page</a>, and click the link <code>Sign up or log in to get your key</code>.

A successful MPAC command will display the message <code>MPAC ran successfully</code>. The requested information will be retrieved and stored in one of four .csv files, depending on the type of information requested.

If MPAC encounters a failure of any kind, diagnostic information will be printed on your screen which should help you to troubleshoot the problem.
