#!/usr/bin/env python
import urllib2
import string
import sys
from httplib import *
from time import gmtime, strftime

#returns the html of a page
def read_page(base_url, extension):
	connection = HTTPConnection(base_url)
	connection.request("GET", extension)
	response = connection.getresponse()
	if response.status == 200:
		page_html = response.read()
		return page_html
	elif response.status == 404:
		raise IOError("Page Not Found")
	else:
		raise IOError(str(response.status) + " " + response.reason)

#main
base_url = "foreignaffairs.com"
try:
	home_html = read_page(base_url, "/articles/140752/bernard-avishai-jalal-al-e-ahmad/among-the-believers")
	print home_html
except IOError, e:
	print e




