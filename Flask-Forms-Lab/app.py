from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

usernames =  {"user1": "pass1", "user2":"pass2"}

facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods = ["GET","POST"])  # '/' for the default page
def login():
	if request.method == "GET":
		return render_template('login.html')
	else:
		if request.form["username"].lower() in usernames and request.form["password"]==usernames[request.form["username"]]:
			return redirect(url_for("home"))
		else:
			return render_template('login.html')
  

@app.route("/home")
def home():
	return render_template("home.html", friends = facebook_friends)

@app.route("/friend_exists/<name>", methods=["GET","POST"])
def friend_exists(name):
	is_friend = name in facebook_friends
	return render_template("friend_exists.html", is_friend=is_friend)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)