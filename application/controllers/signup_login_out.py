#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, session, redirect, url_for
from application.models import user_manager

from flask.ext.wtf import Form
from wtforms import(
	StringField,
	PasswordField,
	RadioField
)
from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms.fields.html5 import DateField

class UserForm(Form):
	email = StringField(
		u'email',
		[
			validators.data_required(message=u'please enter email'),
			validators.Email(message=u'incorrect email form')
		],
		description = {'placeholder' : u'likelion@gmail.com'}
	)
	password = PasswordField(
		u'password',
		[
			validators.data_required(message=u'please enter pass')
		],
		description = {'placeholder' : u'password'}
	)

class SignUpForm(Form):
	username = StringField(
		u'username',
		[
			validators.data_required(message=u'please enter name'),
		],
		description = {'placeholder' : u'likelion'}
	)

	email = StringField(
		u'email',
		[
			validators.data_required(message=u'please enter email'),
			validators.Email(message=u'incorrect email form')
		],
		description = {'placeholder' : u'likelion@gmail.com'}
	)
	password = PasswordField(
		u'password',
		[
			validators.data_required(message=u'please enter pass'),
			validators.length(min=8, max=20, message=u'insert 8~20')
		],
		description = {'placeholder' : u'password'}
	)
	password_check = PasswordField(
		u'password_check',
		[
			validators.data_required(message=u'please enter pass')
		],
		description = {'placeholder' : u'password check'}
	)
	gender = RadioField(u'gender', 
		[validators.data_required(message=u'Select gender')],
		choices=[('M','M'),('F','F')]
	)

	mobile = StringField(
		u'Mobile',
		[
			validators.data_required(message=u'please enter mobilenumber'),
		],
		description = {'placeholder' : u'000-0000-0000'}
	)

	birthday = DateField(
		u'birthday', 
		[
			validators.data_required(message=u'please enter birthday')
		],
		description = {'placeholder' : u'birthday'}
	)


@app.route('/signup', methods=['POST', 'GET'])
def sign_up() :
	form = SignUpForm()

	if request.method == 'POST':
		print "hi validate on submit"
		if form.validate_on_submit():
			user_manager.add_user(form.data)
			return redirect(url_for("show_wall"))

		else:
			print "hi validate on submit222"
			for field in form:
				for error in field.errors:
					print error
			return render_template("sns_signup.html", form = form)
	else:
		print "hi validate on submit333"
		return render_template("sns_signup.html", form = form)

@app.route('/login', methods=['POST', 'GET'])
def log_in() :

	form = UserForm()
	if request.method == 'POST':
		if form.validate_on_submit():			
			email_valid = user_manager.login_check(form.email.data, form.password.data);

			if email_valid:
				session['logged_in'] = True
				
				user = user_manager.find_user_for_login()
				session['email'] = user.email
				session['user_id'] = user.id
				session['user_name'] = user.username

				return redirect(url_for("timeline", wall_id = session['user_id']))
			else:
				login_error = "incorrect"
				return render_template("sns_login.html", form=form, login_error=login_error)
		else:
			pass
	else:
		pass

	return render_template("sns_login.html", form=form)

@app.route('/logout')	
def log_out():
	session.clear()
	return redirect(url_for("index"))
