import bottle, user

secretKey = '12345'

class User_Repository:

	def seed_users(self, users):
		bottle.response.set_cookie('users', users, secretKey)

