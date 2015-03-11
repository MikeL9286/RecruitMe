import bottle, user
from munch import munchify

secretKey = '12345'

class Session_Repository():

	def login(self, user):
		bottle.response.set_cookie('rm', user, secretKey)

	def logout(self):
		bottle.response.delete_cookie('rm')

	def get_logged_in_user(self):
		user = bottle.request.get_cookie('rm', secret=secretKey)
		if user is None:
			return None
		return munchify(user)