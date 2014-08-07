from application import db
from schema import *

def add_user(data):

	print "useruseruseruseruseruseruseruseruseruseruser"
	# pass
	for key in data :
		print data[key]

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
