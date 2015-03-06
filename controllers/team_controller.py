import bottle, team_repository, authentication_repository, user, team
from bottle import get, view, post, put, error, route
from role_type import Role_Type
from itertools import groupby

@get('/teams')
def get_teams():
	currentUser = auth_repo.get_logged_in_user()
	if currentUser is None:
		return bottle.template('login')

	teams = team_repo.get_teams()	
	conferences = set(t.conference for t in teams)

	teams_by_conference = []
	for c in conferences:
		teams_by_conference.append({"name": c, "teams": [t for t in teams if t.conference == c]})

	return bottle.template('teams', {'teams':teams, 'conferences': teams_by_conference})

@get('/teams/<name>')
def get_team(name):
	currentUser = auth_repo.get_logged_in_user()
	if currentUser is None:
		return bottle.template('login')

	teams = team_repo.get_teams()
	team = next((t for t in teams if t.name == name), None)
	return bottle.template('team', {'team':team})

team_repo = team_repository.Team_Repository()
auth_repo = authentication_repository.Authentication_Repository()