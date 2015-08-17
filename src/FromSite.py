#!/usr/bin/python
""" semantics3 API implementation.

"""
from semantics3 import Products
import json

__author__ = "Rajbir Kaur"
__copyright__ = "Copyright 2015"
__license__ = "GPL"
__version__ = "1.0.1"
__status__ = "Prototype"

class FromSite:
	
	def __init__(self, **kwargs):
		self.apikey = kwargs["apikey"]
		self.apisecret = kwargs["apisecret"]
		self.site = kwargs["site"]
		self.limit = 10 	# default and maximum limit is 10.
		self.outpath = kwargs["outpath"]
		self.offset = kwargs["offset"]

	def getData(self):
		
		# Set up a client to talk to the Semantics3 API using your Semantics3 API Credentials
		sem3 = Products(api_key = self.apikey, api_secret = self.apisecret)
		sem3.products_field("site", self.site)
		sem3.products_field("sitedetails_display", ("include", [self.site]))
		sem3.products_field("offset", self.offset)
		sem3.products_field("limit", self.limit)
		results = sem3.get_products()
		ds = json.dumps(results)
		self.writeData(ds)
		return ds

	def writeData(self, ds):
		
		fn = "{}{}.json".format(self.outpath, self.site)
		with open(fn, "w") as wfile:
			wfile.write(ds)
