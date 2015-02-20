import bottle, user

secretKey = '12345'

class User_Repository:

	def seed_users(self, users):
		bottle.response.set_cookie('users', users, secretKey)

	def get_users(self):
		return bottle.request.get_cookie('users', secret=secretKey)

