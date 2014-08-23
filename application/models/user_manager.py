from application import db
from schema import User
from flask import session

def get_user(id):
	return User.query.get(id)

def add_user(data):

	user = User(
		email		= data['email'],
		username	= data['username'],
		gender		= data['gender'],
		password	= db.func.md5(data['password']),
		mobile		= data['mobile'],
		birthday	= data['birthday']
	)

	db.session.add(user)
	db.session.commit()

def login_check(email, password):
	return User.query.filter(User.email == email, User.password == db.func.md5(password)).count() != 0

def add_profile_image(user_id, filename):
	user = get_user(user_id)
	user.profile_image = filename

	db.session.commit()

def get_all() :
	return User.query.all()