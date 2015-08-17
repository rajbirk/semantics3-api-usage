#!/usr/bin/python
""" Main file to initiate code.

"""

import os
import re
import ConfigParser
from src import FromSite

__author__ = "Rajbir Kaur"
__copyright__ = "Copyright 2015"
__license__ = "GPL"
__version__ = "1.0.1"
__status__ = "Prototype"


def getPath():
	
	cwp = os.getcwd()
	return cwp

def getConfInfo(cPath):
	
	config = ConfigParser.ConfigParser()
	config.optionxform = str
	config.read("{}/conf/config.conf".format(cPath))	
	for section in config.sections():
		if re.match(section, "Input"):
			for option in config.options(section):
			        infile = "{}/infile/{}".format(cPath, config.get(section, option))
		if re.match(section, "Credentials"):
			for option in config.options(section):
				if re.match(option, "ApiKey"):
					apikey = config.get(section, option)
				if re.match(option, "ApiSecret"):
					apisecret = config.get(section, option)
		if re.match(section, "Output"):
			for option in config.options(section):
				outpath = config.get(section, option)
				if not os.path.exists(outpath):
					os.makedirs(outpath)

	return (infile, outpath, apikey, apisecret)

if __name__=='__main__':

        cPath = getPath()
        infile, outpath, apikey, apisecret = getConfInfo(cPath)
        
	with open(infile) as f:
		files = f.readlines()

	for fil in files:
		total_results = 20
		offset = 0
		while offset < total_results:
			ifil = fil.strip()
			fsite = FromSite.FromSite(offset=offset, site=ifil, outpath=outpath, apikey=apikey, apisecret=apisecret)
			res = fsite.getData()
			print ds
