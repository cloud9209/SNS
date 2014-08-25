#-*- coding:utf-8 -*-
from application import app
from flask import render_template
from application.models import user_manager

@app.route('/')
@app.route('/index')
def index() :
	return render_template("layout.html")

@app.route('/call_user_list')
def call_user_list() :
	users = user_manager.call_user_list_model()
	return render_template("layout.html", users = users)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404