#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, session, redirect, url_for
from application.models.schema import *
from application.models import user_manager


# User.query.filter(User.name == '')
# user = User.query.get(id)
# user.username = ''
# db.session.commit()


@app.route('/')
@app.route('/index')
def index() :
	user_list = User.query.all()

	return render_template("layout.html", user_list = user_list)

@app.route('/signup', methods=['POST', 'GET'])
def sign_up() :

	if request.method == 'POST':
		user_manager.add_user(request.form);

		return redirect(url_for("show_wall"))

	return render_template("sns_signup.html")


@app.route('/login', methods=['POST', 'GET'])
def log_in() :
	if request.method == 'POST':
		check = user_manager.login_check(request.form['login_email'], request.form['login_password']);
		
		if check == True:
			session['logged_in'] = True
			
			user = User.query.filter(User.email == request.form['login_email']).first()
			session['email'] = user.email
			session['user_id'] = user.id
			session['user_name'] = user.username

			return redirect(url_for("timeline", wall_id = session['user_id']))
		else:
			return render_template("sns_login.html")			
	else:
		pass
	return render_template("sns_login.html")



@app.route('/write_post', methods=['POST', 'GET'])
def write_post() :
	if "secret" in request.form:
		session['post_is_secret'] = 1
	else:
		session['post_is_secret'] = 0

	if request.method == 'POST':
		user_manager.add_post(request.form);
		return redirect(url_for("timeline", wall_id = session['wall_host_id']))
	return render_template("sns_write_post.html")


@app.route('/wall')
def show_wall() :
	return render_template("sns_wall.html")


@app.route('/', defaults={'wall_id':0})
@app.route('/timeline/<int:wall_id>')
def timeline(wall_id):
	user = User.query.get(wall_id)
	posts = user.wall_posts

	session['wall_host_id'] = user.id
	session['wall_host_name'] = user.username

	return render_template("sns_wall.html", wall_host_name = session['wall_host_name'], posts = posts, wall_id = session['wall_host_id'])

@app.route('/delete_post/<int:post_id>', methods=['POST', 'GET'])
def delete_post(post_id):
	if request.method == 'POST':

		post = Post.query.get(post_id)

		db.session.delete(post)
		db.session.commit()

	return redirect(url_for("timeline", wall_id = session['wall_host_id']))

@app.route('/read_post/<int:post_id>')
def read_post(post_id):
	session['read_post_id'] = post_id

	post = Post.query.get(post_id)
	comments = post.comments
	comment_user_name = session['user_name']


	return render_template("sns_read_post.html", comments = comments, post = post, comment_user_name = comment_user_name)



@app.route('/write_comment', methods=['POST', 'GET'])
def write_comment():
	if "secret" in request.form:
		session['comment_is_secret'] = 1
	else:
		session['comment_is_secret'] = 0
	if request.method == 'POST':
		user_manager.add_comment(request.form);

	return redirect(url_for('read_post', post_id = session['read_post_id']))



@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404