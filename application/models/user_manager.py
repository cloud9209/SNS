from application import db
from schema import *
from flask import session
import datetime

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



def add_post(data):
	post = Post(
		body			= data['write_post_box'],
		created_time	= datetime.datetime.now(),
		edited_time		= datetime.datetime.now(),
		is_edited		= 0,
		is_secret		= session['post_is_secret'],
		user_id			= session['user_id'],
		wall_id			= session['wall_host_id']
	)
	db.session.add(post)
	db.session.commit()


def add_comment(data):
	comment = Comment(
		body			= data['comment_box'],
		post_id			= session['read_post_id'],
		user_id			= session['user_id']
	)
	
	db.session.add(comment)
	db.session.commit()
	