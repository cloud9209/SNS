#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, session, redirect, url_for

@app.route('/')
@app.route('/index')
def index() :
	return render_template("layout.html")


'''
	Triggered When 404 NotFound Error Should've been occured
	=> You can make your own View for this error
	=> Something like this : return render_template('404.html')
'''
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404