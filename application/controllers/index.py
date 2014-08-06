#-*- coding:utf-8 -*-
from application import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index() :
	return render_template("layout.html")

@app.route('/signup')
def sign_up() :
	return render_template("sns_signup.html")

@app.route('/login')
def log_in() :
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