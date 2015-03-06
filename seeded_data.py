import bottle, team, user
from role_type import Role_Type

secretKey = '12345'

def seed_all_data():
	seed_users()
	seed_teams()

def seed_users():
	user1 = user.User('user1@email.com', 'p1', 'User 1')
	user2 = user.User('user2@email.com', 'p2', 'User 2')
	user3 = user.User('user3@email.com', 'p3', 'User 3')
	user4 = user.User('user4@email.com', 'p4', 'User 4')
	user4 = user.User('user5@email.com', 'p5', 'User 5')
	
	user1.role = Role_Type.basic
	user2.role = Role_Type.recruit
	user3.role = Role_Type.recruiter
	user3.role = Role_Type.school
	user4.role = Role_Type.admin

	users = [user1, user2, user3, user4]
	bottle.response.set_cookie('users', users, secretKey)

def seed_teams():
	team1 = team.Team('Miami')
	team1.conference = 'ACC'
	team2 = team.Team('Florida State')
	team2.conference = 'ACC'
	team3 = team.Team('Florida')
	team3.conference = 'SEC'
	team4 = team.Team('Ohio State')
	team4.conference = 'B1G'

	teams = [team1, team2, team3, team4]
	bottle.response.set_cookie('teams', teams, secretKey)