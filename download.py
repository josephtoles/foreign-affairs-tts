#!/usr/bin/env python

import requests
import json
from bs4 import BeautifulSoup

#Load login credentials
LOGIN_FILE_NAME = 'credentials'
with open(LOGIN_FILE_NAME, 'r') as f:
	personal_info = json.load(f)
	f.close()

#session
r = requests.Session()

#get form
resp = r.get('https://www.foreignaffairs.com/user?op=lo')
html = resp.raw.read()
soup = BeautifulSoup(html)
tag = soup.find(id='content-area')
tag2 = tag.find(type='hidden')
form_build_id = tag2['id']
print form_build_id

#with open('temp.html', 'w') as f:
#	f.write(html)
#	f.close()


"""
form_build_id = 

credentials = {
	'name': personal_info['email'],
	'pass': personal_info['password'],
	'form_build_id': form_build_id,
	'form_id': 'user_login',
	'op': 'Log in'
}

login_resp = r.post('https://www.foreignaffairs.com/user?destination=home', data=credentials)
"""
