import bottle, user, time
from mongo import Mongo
from munch import munchify

secretKey = '12345'

def get_all():
	users = Mongo().db.users.find()
	return munchifyUsers(users)

def get(query):
	users = Mongo().db.users.find(query)
	return munchifyUsers(users)

def find_one(query):
	user = Mongo().db.users.find_one(query)
	return munchify(user)

def save(user):
	Mongo().db.users.save(user)

def munchifyUsers(users):
	mappedUsers = []
	for user in users:
		mappedUsers.append(munchify(user))
	return mappedUsers