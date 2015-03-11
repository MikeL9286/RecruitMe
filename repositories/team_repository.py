import bottle, team
from munch import munchify

secretKey = '12345'

class Team_Repository:

	def __init__(self, database):
		self.db = database
		self.teams = database.teams

	def get_teams(self):
		teams = bottle.request.get_cookie('teams', secret=secretKey)
		
		return 

	def get_team(self, name):
		teams = bottle.request.get_cookie('teams', secret=secretKey)
		return next((t for t in teams if t.name == name), None)

	def upsert_teams(self, teams):
		bottle.response.set_cookie('teams', teams, secretKey)