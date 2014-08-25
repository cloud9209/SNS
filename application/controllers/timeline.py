@app.route('/wall')
def show_wall() :
	return render_template("sns_wall.html")


@app.route('/', defaults={'wall_id':0})
@app.route('/timeline/<int:wall_id>')
def timeline(wall_id):
	print "timeline hi!!!!!!!!!!!!"
	user = User.query.get(wall_id)
	posts = user.wall_posts

	session['wall_host_id'] = user.id
	session['wall_host_name'] = user.username
	print session['wall_host_id']
	session["scroll_count"] = 0


	return render_template("sns_wall.html", wall_host_name = session['wall_host_name'], posts = posts, wall_id = session['wall_host_id'])

@app.route('/get_5_post', methods=['POST', 'GET'])
def get_5_post():


	if request.method == 'POST':
		all_posts = Post.query.filter(Post.wall_id == session['wall_host_id']).order_by(db.desc(Post.edited_time))
		five_posts = all_posts.slice(int(request.form["offset"]) , int(request.form["offset"])+5)
		
		# if five_posts.count() == 0:
		# 	return ""
	return render_template("sns_wall_2.html", five_posts = five_posts)


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

	post = Post.query.get(post_id)
	comments = post.comments
	comment_user_name = session['user_name']

	return render_template("sns_read_post.html", comments = comments, post = post, comment_user_name = comment_user_name)



@app.route('/revise_post/<int:post_id>', methods=['POST', 'GET'])
def revise_post(post_id):
	post = Post.query.get(post_id)

	if request.method == 'POST':
		# data_manager.revise_post_model(post_id);
		post.body = request.form["write_post_box"]
		db.session.commit()

		return redirect(url_for('read_post', post_id = post_id ))

	return render_template("sns_revise_post.html", post = post)



@app.route('/delete_post/<int:post_id>', methods=['POST', 'GET'])
def delete_post(post_id):
	if request.method == 'POST':
		data_manager.delete_post_model(post_id);

	return redirect(url_for("timeline", wall_id = session['wall_host_id']))
