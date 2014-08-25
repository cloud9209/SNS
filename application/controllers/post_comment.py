#-*- coding:utf-8 -*-
from application import app
from flask import request, session, redirect, url_for
from application.models import data_manager

@app.route('/write_comment', methods=['POST', 'GET'])
def write_comment():
	comment_is_secret = 0
	if "secret" in request.form:
		comment_is_secret = 1
	else:
		pass
	if request.method == 'POST':
		data_manager.add_comment(request.form, comment_is_secret)
	return redirect(url_for('read_post', post_id = session['read_post_id']))

@app.route('/delete_comment/<int:comment_id>', methods=['POST', 'GET'])
def delete_comment(comment_id):
	if request.method == 'POST':
		data_manager.delete_comment_model(comment_id)
	return redirect(url_for("read_post", post_id = session['read_post_id']))
