#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, session
from application.models import user_manager, data_manager

@app.route('/', defaults={'wall_id':0})
@app.route('/timeline/<int:wall_id>')
def timeline(wall_id):
	user = user_manager.get_user(wall_id)
	posts = user.wall_posts
	session['wall_host_id'] = user.id
	session['wall_host_name'] = user.username
	session["scroll_count"] = 0

	return render_template("sns_wall.html", wall_host_name = session['wall_host_name'], posts = posts, wall_id = session['wall_host_id'])

@app.route('/get_posts', methods=['POST', 'GET'])
def get_posts():
	if request.method == 'POST':
		all_posts = data_manager.get_all_posts()		
		five_posts = all_posts.slice(int(request.form["offset"]) , int(request.form["offset"])+5)

	return render_template("sns_wall_2.html", five_posts = five_posts)