#-*- coding:utf-8 -*-
from application import app
<<<<<<< HEAD
from flask import render_template
from application.models import user_manager
=======
from flask import render_template, request, session, redirect, url_for
>>>>>>> 5a8e1c99585f0641650a3b533e85c2fdc65de49b

@app.route('/')
@app.route('/index')
def index() :
	return render_template("layout.html")

<<<<<<< HEAD
@app.route('/call_user_list')
def call_user_list() :
	users = user_manager.call_user_list_model()
	return render_template("layout.html", users = users)

=======

'''
	Triggered When 404 NotFound Error Should've been occured
	=> You can make your own View for this error
	=> Something like this : return render_template('404.html')
'''
>>>>>>> 5a8e1c99585f0641650a3b533e85c2fdc65de49b
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404