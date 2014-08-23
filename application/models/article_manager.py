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

def add_comment(data):
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
