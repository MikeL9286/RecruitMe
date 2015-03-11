import bottle, pymongo, team_repository, session_repository, user_repository, user, team
from bottle import get, view, post, put, error, route
from itertools import groupby

@get('/teams')
def get_teams():
	currentUser = session_repo.get_logged_in_user()
	if currentUser is None:
		return bottle.template('login')

	teams = team_repository.get_teams()
	conferences = set(t.conference for t in teams)

	teams_by_conference = []
	for c in conferences:
		teams_by_conference.append({"name": c, "teams": [t for t in teams if t.conference == c]})

	return bottle.template('teams', {'teams':teams, 'conferences': teams_by_conference})

@get('/teams/<name>')
def get_team(name):
	currentUser = session_repo.get_logged_in_user()
	if currentUser is None:
		return bottle.template('login')

	team = team_repo.get_team(name)
	users = user_repository.get_users()
	commits = [u for u in users if name in u.committed_teams]

	return bottle.template('team', {'team':team, 'commits':commits})

@post('/teams/<name>/commit')
def commit(name):
	user = session_repo.get_logged_in_user()
	user.committed_teams.append(name)
	user_repository.update(user)

	print(user.committed_teams)

	bottle.redirect('/teams/' + name)

@post('teams/<name>/decommit')
def decommit(name):
	user = session_repo.get_logged_in_user()
	user.committed_teams.remove(name)
	user_repository.update(user)
	bottle.redirect('/teams/' + name)

session_repo = session_repository.Session_Repository()