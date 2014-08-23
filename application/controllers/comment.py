from application.models import article_manager

@app.route('/write_comment', methods=['POST', 'GET'])
def write_comment():
	is_comment_secret = [0, 1]['secret' in request.form]
	# use is_comment_secret
	if request.method == 'POST':
		article_manager.add_comment(request.form)

	return redirect(url_for('read_post', post_id = session['read_post_id']))


@app.route('/delete_comment/<int:comment_id>', methods=['POST', 'GET'])
def delete_comment(comment_id):
	if request.method == 'POST':
		data_manager.delete_comment_model(comment_id)

	return redirect(url_for("read_post", post_id = session['read_post_id']))

