# MountainProject API Consumer
## Summary
The MountainProject API Consumer is a (MPAC) small Python program that retrieves data from the <a href=https://www.mountainproject.com/data target="_blank">MountainProject REST APIs</a> and stores the results in comma-separated text (.csv) files.

## Requirements
To run MPAC, Python version 3+ must be installed on your computer. <i>You can download and install the latest Python version <a href=https://www.python.org/downloads target="_blank">here</a></i>.

## Install the MountainProject API Consumer
Use one of the following methods to install MPAC on your computer:
* If Git is installed, navigate to a clean directory on your file system and type <code>git clone https<nolink>://github.com/dchampion/mp-dump.git</code>. This will install MPAC into a subdirectory called <code>mp-dump</code>.

* Alternatively, if <code>Git</code> is not installed, or you do not wish to use it, click the <code>Clone or download</code> button on this page to download and extract a zipped version of MPAC into a clean file system directory.

## Set Up a (Virtual) Environment
To avoid polluting your global Python environment with the dependencies required by MPAC, set up and activate a virtual environment.

* Install your virtual environment:

    * From the directory into which you cloned/installed MPAC, type <code>python -m venv .venv</code>

* Activate your virtual environment:

    * If using a Unix-based shell like <code>bash</code>, or a MacOS terminal, type <code>source .venv/Scripts/activate</code>

    * If using a Windows-based shell like <code>cmd</code> or <code>PowerShell</code>, type <code>".venv/Scripts/activate.bat"</code> (you must include the double-quotes for this command to work in a Windows-based shell).

* Install the MPAC dependencies into your virtual environment:

    * Type <code>pip install -r requirements.txt</code>

With the successful completion of these three steps, you should be ready to consume the MountainProject REST APIs.

## Run the MountainProject API Consumer
Type <code>python mp.py</code> to display a comprehensive help page, including examples, for using MPAC.

<b>IMPORTANT:</b> You will need to supply a valid MountainProject-supplied user key to execute any and all requests with MPAC (the key used in the examples will not work). To get your private key, go to the <a href=https://www.mountainproject.com/data>MountainProject API page</a>, and click the link <code>Sign up or log in to get your key</code>.

A successful MPAC command will display the message <code>MPAC ran successfully</code>. The requested information will be retrieved and stored in one of four .csv files, depending on the type of information requested.

If MPAC encounters a failure of any kind, diagnostic information will be printed on your screen which should help you to troubleshoot the problem.
