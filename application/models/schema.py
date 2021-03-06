from application import db

#make user table

class User(db.Model):
	#table colum name
	id			= db.Column(db.Integer, primary_key = True)
	email		= db.Column(db.String(60))
	username	= db.Column(db.String(45))
	gender 		= db.Column(db.Enum('F', 'M'))
	password	= db.Column(db.String(100))
	mobile		= db.Column(db.String(15))
	birthday	= db.Column(db.Date)
	profile_image = db.Column(db.String(100))

class Post(db.Model):
	id				= db.Column(db.Integer, primary_key = True)
	body			= db.Column(db.Text())
	created_time	= db.Column(db.DateTime)
	edited_time 	= db.Column(db.DateTime)
	is_edited		= db.Column(db.Boolean)
	is_secret		= db.Column(db.Boolean)
#foreign key
	user_id			= db.Column(db.Integer, db.ForeignKey('user.id')) #only user_id
	user			= db.relationship('User', foreign_keys = [user_id]) 
	#to get all the info. of the user we got
	wall_id			= db.Column(db.Integer, db.ForeignKey('user.id'))
	wall			= db.relationship('User', foreign_keys = [wall_id], backref = db.backref('wall_posts', cascade = 'all, delete-orphan', lazy = 'dynamic'))

class Comment(db.Model):
	id				= db.Column(db.Integer, primary_key = True)
	body			= db.Column(db.Text())
	is_secret		= db.Column(db.Boolean)
	created_time	= db.Column(db.DateTime, default = db.func.now())
	post_id			= db.Column(db.Integer, db.ForeignKey('post.id'))
	Post 			= db.relationship('Post', backref = db.backref('comments', cascade = 'all, delete-orphan', lazy = 'dynamic'))	
	user_id			= db.Column(db.Integer, db.ForeignKey('user.id'))
	user			= db.relationship('User')


class Follow(db.Model):
	id 			= db.Column(db.Integer, primary_key = True)
	follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	follower	= db.relationship('User', foreign_keys = [follower_id], backref = db.backref('followees', cascade = 'all, delete-orphan', lazy = 'dynamic'))
	followee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	followee	= db.relationship('User', foreign_keys = [followee_id], backref = db.backref('followers', cascade = 'all, delete-orphan', lazy = 'dynamic'))






