import bottle, authentication_repository, user
from bottle import get, view, post, error, route
from role_type import Role_Type

@get('/profile')
def get_profile():
	currentUser = auth_repo.get_logged_in_user()
	if currentUser is None:
		return bottle.template('login')

	return bottle.template('profile', {'user':currentUser})

auth_repo = authentication_repository.Authentication_Repository()