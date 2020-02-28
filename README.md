# MountainProject API Consumer
## Summary
A small Python program that retrieves data from the <a href=https://www.mountainproject.com/data target="_blank">Mountain Project REST APIs</a> and stores the results in comma-separated text (.csv) files.

## Requirements
To run this app, Python version 3+ must be installed on your computer. <i>You can download and install the latest Python versions <a href=https://www.python.org/downloads target="_blank">here</a></i>.

## Install the MountainProject API Consumer
Use one of the following methods to install the MountainProject API Consumer on your computer:
* If Git is installed, navigate to a clean directory on your file system and type <code>git clone https<nolink>://github.com/dchampion/mp-dump.git</code>. This will install the app in a subdirectory called <code>mp-dump</code>.

* Alternatively, if <code>Git</code> is not installed, or you do not wish to use it, use links on this page to download and extract a zipped version of the app into a clean file system directory.

## Set Up a (Virtual) Environment
To avoid polluting your global Python installation with the dependencies required by this app, set up and activate a virtual environment.
* Install your virtual environment. From the directory into which you cloned/installed this app, type <code>python -m venv .venv</code>
* Activate your virtual environment:

    * If using *nix (e.g. a Unix-based operating system like Linux), type <code>source .venv/Scripts/activate</code>

    * If using Windows, type <code>".venv/Scripts/activate.bat"</code> (note that double-quotes are required).

* Install dependencies into your virtual environment. Type <code>pip install -r requirements.txt</code>

With the successful completion of these three steps, you should be ready to consume the Mountain Project REST APIs.

## Run the Mountain Project API Consumer
Type <code>python mp.py</code> to display a help screen, with examples, for using the app.

<b>IMPORTANT:</b> You will need to supply a valid Mountain Project-supplied user key to execute any and all requests with this app (the key used in the examples will not work). To get your private key, go to the <a href=https://www.mountainproject.com/data>Mountain Project API page</a>, and click the link <i>Sign up or log in to get your key</i>.

If the app is successful in retrieving the requested information, it will silently return and store the results in one of four .csv files, depending on the type of information requested.

If there is a failure of any kind, diagnostic information will be printed on your screen which should help you to troubleshoot the problem.