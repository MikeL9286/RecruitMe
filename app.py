#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

import bottle
from bottle import default_app, request, route, response, get, error

bottle.debug(True)

secretKey = '12345'

@get('/')
@bottle.view('index')
def show_login():
	seed_users()
	return {'username':'', 'password':'', 'message':''}

@bottle.post('/login')
def login():
	username = bottle.request.forms.get("username")
	password = bottle.request.forms.get("password")
	users = bottle.request.get_cookie('users', secret=secretKey)

	for user in users:
		if user['username'] == username and user['password'] == password:
			return bottle.template('welcome', dict(username=username))

	print(username + ' not found.')
	return bottle.redirect('/')

def seed_users():
	user1 = {'username':'user1', 'password':'p1'}
	user2 = {'username':'user2', 'password':'p2'}
	user3 = {'username':'user3', 'password':'p3'}
	users = [user1, user2, user3]
	bottle.response.set_cookie('users', users, secretKey)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

bottle.run(host='0.0.0.0', port=argv[1])