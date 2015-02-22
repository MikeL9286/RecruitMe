import bottle, user, user_repository

secretKey = '12345'

class Authentication_Repository:

	def login(self, user):
		bottle.response.set_cookie('user', user, secretKey)

	def logout(self):
		bottle.response.delete_cookie('user')

	def get_logged_in_user(self):
		return bottle.request.get_cookie('user', secret=secretKey)