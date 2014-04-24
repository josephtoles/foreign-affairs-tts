#!/usr/bin/env python

import requests
import json
from bs4 import BeautifulSoup

#Returns a session to use
def login():
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
	return r

#Use this function only after logging in.
#r is the session returned from logging on
def get_html(url, r):
	resp = r.get(url)
	html = resp.raw.read()
	with open('temp.html', 'w') as f:
		f.write(html)
		f.close()
	return html

def get_article_text(url, r):
	full = ''
	resp = r.get(url)
	html = resp.raw.read()
	soup = BeautifulSoup(html)

	title = soup.h1.get_text()
	subtitle = soup.h2.get_text()
	author = soup.find(is_author).get_text()
	article = soup.find(is_article).get_text()

	output = title+'.\n'+subtitle+'.'+author+'.'+article
	return output

def is_article(tag):
	return tag.has_attr('class') and tag['class'][0] == 'content-resize'

def is_author(tag):
	return tag.has_attr('class') and tag['class'][0] == 'article-field-authors'
