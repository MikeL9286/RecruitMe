import bottle, user, time
from mongo import Mongo
from munch import munchify

secretKey = '12345'

def get_all():
	return __dict__.update(Mongo().db.users.find())

def get(query):
	return Mongo().db.users.find(query)

def find_one(query):
	return munchify(Mongo().db.users.find_one(query))

def save(user):
	Mongo().db.users.save(user)
	# bottle.response.delete_cookie('user')
	# bottle.response.set_cookie('user', user, secretKey)
	# users = bottle.request.get_cookie('users', secret=secretKey)
	# users.append(user)
	# update_users(user)