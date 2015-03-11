import bottle, team
from mongo import Mongo
from munch import munchify

secretKey = '12345'

def get_teams():
	teams = Mongo().db.teams.find()
	return munchifyTeams(teams)

def get_team(name):
	team = Mongo().db.teams.find_one({'name':name})
	return munchify(team)

def upsert_teams(teams):
	bottle.response.set_cookie('teams', teams, secretKey)

def munchifyTeams(teams):
	mappedTeams = []
	for team in teams:
		mappedTeams.append(munchify(team))
	return mappedTeams