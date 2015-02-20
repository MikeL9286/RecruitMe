import bottle, authentication_repository, user_repository, user
from bottle import get, view, post, error

@get('/')
@view('index')
def get_login():
	currentUser = auth_repo.get_logged_in_user()
	if (currentUser is not None):
		return bottle.template('welcome', {'username':currentUser.user_name})

	if (user_repo.get_users() is None):
		seed_users()

	return {'username':'', 'password':'', 'message':''}

@post('/login')
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
	return bottle.template('index', {'username':'', 'password':'', 'message':'Invalid username and/or password.'})

@get('/logout')
def logout():
	auth_repo.logout()
	return bottle.redirect('/')

def seed_users():
	user1 = user.User('user1', 'p1')
	user2 = user.User('user2', 'p2')
	user3 = user.User('user3', 'p3')
	user_repo.seed_users([user1, user2, user3])

auth_repo = authentication_repository.Authentication_Repository()
user_repo = user_repository.User_Repository()