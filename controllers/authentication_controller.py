import bottle, authentication_repository, user_repository, user
from bottle import get, view, post, error, route

@get('/')
@view('login')
def get_login():
	currentUser = auth_repo.get_logged_in_user()
	if (currentUser is not None):
		return bottle.template('welcome', {'fullName':currentUser.full_name})

	if (user_repo.get_users() is None):
		seed_users()

	return

@post('/login')
@view('welcome')
def login():
	email = bottle.request.forms.get('email')
	password = bottle.request.forms.get('password')
	users = user_repo.get_users()

	for user in users:
		if user.email == email and user.password == password:
			auth_repo.login(user)
			return {'fullName':user.full_name}

	return bottle.template('login', {'email':email, 'password':'', 'error':'Invalid username and/or password.'})

@get('/signup')
@view('signUp')
def signUp():
	currentUser = auth_repo.get_logged_in_user()
	if (currentUser is not None):
		return bottle.template('welcome', {'fullName':currentUser.full_name})

	return

@post('/signup')
@view('welcome')
def login():
	fullName = bottle.request.forms.get('fullName')
	email = bottle.request.forms.get('email')
	password = bottle.request.forms.get('password')
	passwordCheck = bottle.request.forms.get('passwordCheck')
	users = user_repo.get_users()

	for user in users:
		if user.user_name == username:
			return bottle.template('login', {'fullName':fullName, 'email':email, 'password':password, 'passwordCheck':passwordCheck, 'error':'E-mail already exists.'})

	if password != passwordCheck:
		return bottle.template('login', {'fullName':fullName, 'email':email, 'password':password, 'passwordCheck':passwordCheck, 'error':'Passwords do not match.'})
	
	# TODO
	# add user to list

	return {'fullName':fullName}

@get('/logout')
def logout():
	auth_repo.logout()
	return bottle.redirect('/')

def seed_users():
	user1 = user.User('user1@email.com', 'p1', 'User 1')
	user2 = user.User('user2@email.com', 'p2', 'User 2')
	user3 = user.User('user3@email.com', 'p3', 'User 3')
	user_repo.seed_users([user1, user2, user3])

auth_repo = authentication_repository.Authentication_Repository()
user_repo = user_repository.User_Repository()