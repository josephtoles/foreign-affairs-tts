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

#log in (requires foreign affairs account)
resp = r.get('https://www.foreignaffairs.com/user?op=lo')
html = resp.raw.read()
soup = BeautifulSoup(html)
form_build_id = soup.find(id='content-area').find(type='hidden')['id']

credentials = {
	'name': personal_info['email'],
	'pass': personal_info['password'],
	'form_build_id': form_build_id,
	'form_id': 'user_login',
	'op': 'Log in'
}

login_resp = r.post('https://www.foreignaffairs.com/user?destination=home', data=credentials)

resp = r.get('http://www.foreignaffairs.com/articles/141353/halil-karaveli/cold-turkey')
html = resp.raw.read()

with open('temp.html', 'w') as f:
	f.write(html)
	f.close()
