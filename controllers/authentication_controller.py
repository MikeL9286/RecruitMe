import bottle, session_repository, user_repository, user, role_type
from bottle import get, view, post, error, route, request

@get('/')
@view('login')
def get_login():
	user = session_repo.get_logged_in_user()
	if user is not None:
		return bottle.redirect('/dashboard')
	return

@post('/login')
def login():
	email = request.forms.get('email')
	password = request.forms.get('password')
	user = user_repository.find_one({'email':email,'password':password})

	if user is None:
		return bottle.template('login', {'email':email, 'password':'', 'error':'Invalid username and/or password.'})

	session_repo.login(user)
	return bottle.redirect('/dashboard')

@get('/signup')
@view('signUp')
def get_signup():
	currentUser = session_repo.get_logged_in_user()
	if (currentUser is not None):
		return bottle.redirect('/dashboard')
	return

@post('/signup')
def signup():
	fullName = request.forms.get('fullName')
	email = request.forms.get('email')
	password = request.forms.get('password')
	passwordCheck = request.forms.get('passwordCheck')
	
	existingUser = user_repository.find_one({'email':email})

	if existingUser is not None:
		return bottle.template('signUp', {'fullName':fullName, 'email':email, 'password':password, 'passwordCheck':passwordCheck, 'error':'E-mail already exists.'})

	if password != passwordCheck:
		return bottle.template('signUp', {'fullName':fullName, 'email':email, 'password':password, 'passwordCheck':passwordCheck, 'error':'Passwords do not match.'})

	newUser = user.User(email, password, fullName)
	user_repository.save(newUser)
	session_repo.login(newUser)
	return bottle.redirect('/dashboard')

@get('/logout')
def logout():
	session_repo.logout()
	return bottle.redirect('/')

session_repo = session_repository.Session_Repository()