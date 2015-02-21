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
			auth_repo.login(user);
			return {'fullName':user.full_name}

	print(email + ' not found.')
	return bottle.template('login', {'loginEmail':email, 'password':'', 'loginError':'Invalid username and/or password.'})

@post('/signUp')
@view('welcome')
def login():
	username = bottle.request.forms.get('username')
	password = bottle.request.forms.get('password')
	users = user_repo.get_users()

	for user in users:
		if user.user_name == username and user.password == password:
			auth_repo.login(user);
			return {'username':username}

	print(username + ' not found.')
	return bottle.template('login', {'email':'', 'password':'', 'loginError':'Invalid username and/or password.'})

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