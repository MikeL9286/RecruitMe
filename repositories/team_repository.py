import bottle, team

secretKey = '12345'

class Team_Repository:

	def get_teams(self):
		return bottle.request.get_cookie('teams', secret=secretKey)

	def seed_teams(self, teams):
		bottle.response.set_cookie('teams', teams, secretKey)