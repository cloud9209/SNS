from application import app
from flask import render_template, request, session, redirect, url_for
from application.models import user_manager, data_manager

@app.route('/write_post', methods=['POST', 'GET'])
def write_post() :
	if "secret" in request.form:
		session['post_is_secret'] = 1
	else:
		session['post_is_secret'] = 0
	if request.method == 'POST':
		data_manager.add_post(request.form);
		return redirect(url_for("timeline", wall_id = session['wall_host_id']))
	return render_template("sns_write_post.html")

@app.route('/read_post/<int:post_id>')
def read_post(post_id):
	session['read_post_id'] = post_id

	post = data_manager.get_post_by_id(post_id)
	comments = post.comments
	comment_user_name = session['user_name']
	return render_template("sns_read_post.html", comments = comments, post = post, comment_user_name = comment_user_name)

@app.route('/revise_post/<int:post_id>', methods=['POST', 'GET'])
def revise_post(post_id):
	post = data_manager.get_post_by_id(post_id)

	if request.method == 'POST':
		post.body = request.form["write_post_box"]
		db.session.commit()
		return redirect(url_for('read_post', post_id = post_id ))
	return render_template("sns_revise_post.html", post = post)

@app.route('/delete_post/<int:post_id>', methods=['POST', 'GET'])
def delete_post(post_id):
	if request.method == 'POST':
		data_manager.delete_post_model(post_id);
	return redirect(url_for("timeline", wall_id = session['wall_host_id']))
