#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, session
from application.models.schema import *
from application.models import user_manager


# User.query.filter(User.email == '')
# user = User.query.get(id)
# user.username = ''
# db.session.commit()

# user = User.query.get(id)
# db.session.delete(user)
# db.session.commit()

@app.route('/')
@app.route('/index')
def index() :
	return render_template("layout.html")

@app.route('/signup', methods=['POST', 'GET'])
def sign_up() :

	if request.method == 'POST':
		user_manager.add_user(request.form);

	return render_template("sns_signup.html")


@app.route('/login', methods=['POST', 'GET'])
def log_in() :
	if request.method == 'POST':
		check = user_manager.login_check(request.form['login_email'], request.form['login_password']);
		
		if check == True:
			session['logged_in'] = True

			print "good"
			return render_template("sns_wall.html", login_user_name = request.form['login_email'])
		else:
			return render_template("sns_login.html")			
	else:
		pass
	return render_template("sns_login.html")

@app.route('/write_post')
def write_post() :
	return render_template("sns_write_post.html")

@app.route('/wall')
def show_wall() :
	return render_template("sns_wall.html")

@app.route('/read_post')
def read_post():
	return render_template("sns_read_post.html")

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404