from application import app
from flask import render_template, request, session
from application.models import user_manager, data_manager

@app.route('/newsfeed')
def newsfeed():	
	return render_template("sns_newsfeed.html" )

@app.route('/get_5_post_newsfeed', methods=['POST', 'GET'])
def get_5_post_newsfeed():
	celebrities = []
	user = user_manager.get_user(session['user_id'])

	followees = user.followees
	for followee in followees:
		celebrities.append(followee.followee_id)

	if request.method == 'POST':
		all_posts = data_manager.newsfeed_get_all_posts(celebrities)		
		five_posts = all_posts.slice(int(request.form["offset"]) , int(request.form["offset"])+5)

	return render_template("sns_newsfeed_2.html", five_posts = five_posts)
