import bottle, authentication_repository, user_repository, user
from bottle import get, view, post, put, error, route
from role_type import Role_Type

@get('/profile')
def get_profile():
	currentUser = auth_repo.get_logged_in_user()
	if currentUser is None:
		return bottle.template('login')

	return bottle.template('profile', {'user':currentUser})

@post('/update-email')
def update_email():
	email = bottle.request.forms.get('email')
	users = user_repo.get_users()
	currentUser = auth_repo.get_logged_in_user()

	if any(u.email == email for u in users):
		return bottle.template('profile', {'user':currentUser, 'message':'The e-mail already exists.'})

	# validate email format
	
	currentUser.email = email
	user_repo.update(currentUser)
	
	return bottle.template('profile', {'user':currentUser, 'message':'Success.'})


@put('/update-password')
def update_password():
	oldPassword = bottle.request.forms.get('oldPassword')
	newPassword = bottle.request.forms.get('newPassword')
	passwordCheck = bottle.request.forms.get('passwordCheck')
	currentUser = auth_repo.get_logged_in_user()

	if currentUser.password != oldPassword:
		return bottle.template('profile', {'user':currentUser, 'message':'The old password is incorrect.'})

	if newPassword != passwordCheck:
		return bottle.template('profile', {'user':currentUser, 'message':'The passwords do not match.'})

	currentUser.password = newPassword
	user_repo.update(currentUser)

	return bottle.template('profile', {'user':currentUser, 'message':'Success.'})

@put('/update-name')
def update_name():
	fullName = bottle.request.forms.get('name')
	currentUser = auth_repo.get_logged_in_user()

	currentUser.full_name = fullName
	user_repo.update(currentUser)

	return bottle.template('profile', {'user':currentUser, 'message':'Success.'})

auth_repo = authentication_repository.Authentication_Repository()
user_repo = user_repository.User_Repository()