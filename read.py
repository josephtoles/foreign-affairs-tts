#!/usr/bin/env python

import download
import sys
import os

OUTPUT_FILE_NAME = 'output_temp'

r = download.login()
if len(sys.argv) == 1:
	print "Please enter a url"
	sys.exit()
url = sys.argv[1]
output = download.get_article_text(url, r)
with open(OUTPUT_FILE_NAME, 'w') as f:
	f.write(output.encode('utf8'))
	f.close()
os.system('festival --tts '+OUTPUT_FILE_NAME)
