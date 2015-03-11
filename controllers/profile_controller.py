import bottle, pymongo, session_repository, user_repository, user
from bottle import get, view, post, put, error, route

@get('/profile')
def get_profile():
	currentUser = session_repo.get_logged_in_user()
	if currentUser is None:
		return bottle.template('login')

	print(currentUser)
	return bottle.template('profile', {'user':currentUser})

@post('/update-email')
def update_email():
	email = bottle.request.forms.get('email')
	users = user_repository.get_users()
	currentUser = session_repo.get_logged_in_user()

	if any(u.email == email for u in users):
		return bottle.template('profile', {'user':currentUser, 'message':'The e-mail already exists.'})

	# validate email format
	
	currentUser.email = email
	user_repository.update(currentUser)
	
	return bottle.template('profile', {'user':currentUser, 'message':'Success.'})

@post('/validate-email')
def validate_email():
	email = bottle.request.forms.get('email')
	users = user_repository.get_users()
	if any(u.email == email for u in users):
		return {'valid':False}
	return {'valid':True}


@post('/update-password')
def update_password():
	oldPassword = bottle.request.forms.get('oldPassword')
	newPassword = bottle.request.forms.get('newPassword')
	passwordCheck = bottle.request.forms.get('passwordCheck')
	currentUser = session_repo.get_logged_in_user()

	if currentUser.password != oldPassword:
		return bottle.template('profile', {'user':currentUser})

	if newPassword != passwordCheck:
		return bottle.template('profile', {'user':currentUser})

	if validatePasswordRequirements(newPassword):
		return bottle.template('profile', {'user':currentUser})

	currentUser.password = newPassword
	user_repository.update(currentUser)

	return bottle.template('profile', {'user':currentUser})

def validatePasswordRequirements(password):
     # var hasEightCharacters = password.length >= 8;
     # var hasUpperCase = /[A-Z]/.test(password);
     # var hasLowerCase = /[a-z]/.test(password);
     # var hasNumbers = /\d/.test(password);
     # var hasNonalphas = /\W/.test(password);
     # return hasEightCharacters && hasUpperCase && hasLowerCase && hasNumbers && hasNonalphas;
     return true

@post('/update-name')
def update_name():
	fullName = bottle.request.forms.get('name')
	currentUser = session_repo.get_logged_in_user()

	currentUser.full_name = fullName
	user_repository.update(currentUser)

	return bottle.template('profile', {'user':currentUser, 'message':'Success.'})

session_repo = session_repository.Session_Repository()