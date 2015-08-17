# semantics3-api-usage

Python implementation of semantics3 API. This code extracts the website data using API.
The results obtained are in JSON format so its convenient for users to use the results 
as they like.


configuration
===================
Config file is present in conf directory under code folder. Parameters that you can edit 
through the conf file are:

a) Input:	It contains the filename that contains the list of websites. 
			This file is present in infile directory under code folder.
b) Output: 	It contain the output path where the results obtained will be stored.


code execution
=================
Before executing the code you would like to make some configuration changes to the code. 
You can make these changes through config.conf file present in conf directory under code 
folder. Refer configuration part for more information.

a) Open command line.

b) Change directory to path containing code folder like:
   cd /path/to/code
   
c) Then type in command line:
   python main.py
   This will extract data from the website and save the json result file to the specified 
   location as well as print the result to console also.



