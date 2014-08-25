from application import db
from schema import *
from flask import session
import datetime

def call_user_list_model():
	return User.query.all()

def find_user_list_model():	
	return User.query.filter(User.username.like('%' + character + '%')).all()

def find_user_for_login():
	return User.query.filter(User.email == request.form['email']).first()

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

def get_post_by_id(post_id):
	return Post.query.get(post_id)

def get_all_posts():
	return Post.query.filter(Post.wall_id == session['wall_host_id']).order_by(db.desc(Post.edited_time))

def newsfeed_get_all_posts(celebrities):
	return Post.query.filter( (Post.wall_id == session['user_id']) | (Post.user_id == session['user_id']) | (Post.user_id.in_(celebrities) ) | \
										(Post.wall_id.in_(celebrities))).order_by(db.desc(Post.edited_time))