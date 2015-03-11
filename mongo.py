from pymongo import MongoClient

class Mongo():
	@property
	def db(self):
	    return type(self)._db

	@db.setter
	def db(self, connection_string):
		print('Connecting at ' + connection_string + '...')
		type(self)._db = MongoClient(connection_string).recruitme	