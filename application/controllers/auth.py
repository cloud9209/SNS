@app.route('/user_list')
def user_list() :
	return render_template("layout.html", users = user_manager.get_all())

@app.route('/find_user_list', methods=['POST', 'GET'])
def find_user_list():

	if request.method == 'POST':
		character = request.form["character"]
		

		found_user_list = User.query.filter(User.username.like('%' + character + '%')).all()

		return render_template("sns_follow_2.html", found_user_list = found_user_list)

	return render_template("sns_follow.html")



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


