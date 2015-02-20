import bottle, user_repository, user
from bottle import get, view, post, error

@get('/')
@view('index')
def show_login():
	seed_users()
	return {'username':'', 'password':'', 'message':''}

@post('/login')
def login():
	username = bottle.request.forms.get("username")
	password = bottle.request.forms.get("password")
	users = bottle.request.get_cookie('users', secret=secretKey)

	for user in users:
		if user.user_name == username and user.password == password:
			return bottle.template('welcome', dict(username=username))

	print(username + ' not found.')
	return bottle.redirect('/')

def seed_users():
	user1 = user.User('user1', 'p1')
	user2 = user.User('user2', 'p2')
	user3 = user.User('user3', 'p3')
	user_repo.seed_users([user1, user2, user3])

secretKey = '12345'
user_repo = user_repository.User_Repository()