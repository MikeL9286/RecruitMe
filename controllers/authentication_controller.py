import bottle, authentication_repository, user_repository, user
from bottle import get, view, post, error, route

@get('/')
@view('login')
def get_login():
	currentUser = auth_repo.get_logged_in_user()
	if currentUser is not None:
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
			return {'user':user}

	return bottle.template('login', {'email':email, 'password':'', 'error':'Invalid username and/or password.'})

@get('/signup')
@view('signUp')
def get_signup():
	currentUser = auth_repo.get_logged_in_user()
	if (currentUser is not None):
		return bottle.template('welcome', {'fullName':currentUser.full_name})

	return

@post('/signup')
@view('welcome')
def signup():
	fullName = bottle.request.forms.get('fullName')
	email = bottle.request.forms.get('email')
	password = bottle.request.forms.get('password')
	passwordCheck = bottle.request.forms.get('passwordCheck')
	users = user_repo.get_users()

	if any(u.email == email for u in users):
		return bottle.template('signUp', {'fullName':fullName, 'email':email, 'password':password, 'passwordCheck':passwordCheck, 'error':'E-mail already exists.'})

	if password != passwordCheck:
		return bottle.template('signUp', {'fullName':fullName, 'email':email, 'password':password, 'passwordCheck':passwordCheck, 'error':'Passwords do not match.'})

	newUser = user.User(email, password, fullName)
	users.append(newUser)
	user_repo.seed_users(users)
	auth_repo.login(newUser)

	return {'user':newUser}

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