import bottle, team_repository, authentication_repository, user, team
from bottle import get, view, post, put, error, route
from role_type import Role_Type

@get('/teams')
def get_teams():
	currentUser = auth_repo.get_logged_in_user()
	if currentUser is None:
		return bottle.template('login')

	teams = team_repo.get_teams()
	if (teams is None):
		seed_teams()
	teams = team_repo.get_teams()

	return bottle.template('teams', {'teams':teams})

@get('/teams/<name>')
def get_team(name):
	currentUser = auth_repo.get_logged_in_user()
	if currentUser is None:
		return bottle.template('login')

	teams = team_repo.get_teams()
	team = next((t for t in teams if t.name == name), None)

	return bottle.template('team', {'team':team})

def seed_teams():
	team1 = team.Team('Miami')
	team2 = team.Team('Florida State')
	team3 = team.Team('Florida')
	team_repo.seed_teams([team1, team2, team3])

team_repo = team_repository.Team_Repository()
auth_repo = authentication_repository.Authentication_Repository()