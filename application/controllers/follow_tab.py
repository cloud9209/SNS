#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, session
from application.models import user_manager, data_manager

@app.route('/find_user_list', methods=['POST', 'GET'])
def find_user_list():
	if request.method == 'POST':
		character = request.form["character"]
		found_user_list = user_manager.find_user_list_model()
		return render_template("sns_follow_2.html", found_user_list = found_user_list)
	return render_template("sns_follow.html")


@app.route('/add_follow_user_controllers', methods=['POST', 'GET'])
def add_follow_user_controllers():
	if request.method == 'POST':	
		data_manager.add_follow_user_model(request.form['user_id'])
		who_I_follow = data_manager.get_who_I_follow(session['user_id'])
		return render_template("add_follow_user.html", who_I_follow = who_I_follow)
