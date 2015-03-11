import bottle, session_repository, user, role_type
from bottle import get

@get('/dashboard')
def get_login():
	user = session_repo.get_logged_in_user()
	if user is None:
		return bottle.redirect('/')

	return render_dashboard_by_role(user)

def render_dashboard_by_role(user):
	if user.role == role_type.recruit:
		return bottle.template('dashboard_recruit', {'user':user})

	if user.role == role_type.recruiter:
		return bottle.template('dashboard_recruiter', {'user':user})

	if user.role == role_type.school:
		return bottle.template('dashboard_school', {'user':user})

	if user.role == role_type.admin:
		return bottle.template('dashboard_admin', {'user':user})	

	return bottle.template('dashboard_basic', {'user':user})

session_repo = session_repository.Session_Repository()