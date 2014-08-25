from application import db
from schema import *
from flask import session
import datetime

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

def delete_post_model(post_id):
	post = Post.query.get(post_id)
	db.session.delete(post)
	db.session.commit()

def add_comment(data, is_secret):
	comment = Comment(
		body			= data['comment_box'],
		post_id			= session['read_post_id'],
		user_id			= session['user_id']

	)
	
	db.session.add(comment)
	db.session.commit()
	
def delete_comment_model(comment_id):
	comment = Comment.query.get(comment_id)
	db.session.delete(comment)
	db.session.commit()

def add_follow_user_model(user_id):
	follow_user = User.query.filter(User.id == user_id).first()

	follow = Follow(
		follower_id = session['user_id'],
		followee_id = follow_user.id
		)
	db.session.add(follow)
	db.session.commit()

def get_who_I_follow(user_id):
	print "hi man get_who_I_follow"
	who_I_follow_list = Follow.query.filter(Follow.follower_id == user_id).all()
	print "hi man get_who_I_follow2222"
	return who_I_follow_list


def get_post_by_id(post_id):
	return Post.query.get(post_id)

def get_all_posts():
	return Post.query.filter(Post.wall_id == session['wall_host_id']).order_by(db.desc(Post.edited_time))

def newsfeed_get_all_posts(celebrities):
	return Post.query.filter( (Post.wall_id == session['user_id']) | (Post.user_id == session['user_id']) | (Post.user_id.in_(celebrities) ) | \
										(Post.wall_id.in_(celebrities))).order_by(db.desc(Post.edited_time))




