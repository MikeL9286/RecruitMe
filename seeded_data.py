import user, team, role_type
from mongo import Mongo

def seed_all_data():
	if Mongo().db.users.count() == 0:
		seed_users()

	if Mongo().db.teams.count() == 0:
		seed_teams()

def seed_users():
	print('-SEEDING USERS-')
	user1 = user.User('user1@email.com', 'p1', 'User 1')
	user2 = user.User('user2@email.com', 'p2', 'User 2')
	user3 = user.User('user3@email.com', 'p3', 'User 3')
	user4 = user.User('user4@email.com', 'p4', 'User 4')
	user4 = user.User('user5@email.com', 'p5', 'User 5')
	
	user1.role = role_type.basic
	user2.role = role_type.recruit
	user3.role = role_type.recruiter
	user3.role = role_type.school
	user4.role = role_type.admin

	users = [user1, user2, user3, user4]
	users = [u.__dict__ for u in users]
	Mongo().db.users.insert(users)

def seed_teams():
	print('-SEEDING TEAMS-')
	team1 = team.Team('Miami')
	team1.conference = 'ACC'
	team2 = team.Team('Florida State')
	team2.conference = 'ACC'
	team3 = team.Team('Florida')
	team3.conference = 'SEC'
	team4 = team.Team('Ohio State')
	team4.conference = 'B1G'

	teams = [team1, team2, team3, team4]
	teams = [t.__dict__ for t in teams]
	Mongo().db.teams.insert(teams)