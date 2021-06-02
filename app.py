import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# Creates an instance of Flask stored in variable 'app'.
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/view_recipe")
def view_recipe():
    recipes = mongo.db.recipes.find()
    return render_template("view-recipe.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checks the database for existing user
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        elif existing_email:
            flash("Email already exists")
            return redirect(url_for("register"))

        register = {
            "fname": request.form.get("fname").lower(),
            "lname": request.form.get("lname").lower(),
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return render_template("index.html")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checks the database for existing user
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # checks db password and entered password match
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return render_template("index.html")
                    # return redirect(url_for("profile", username=session["user"]))
            else:
                # below occurs if passwords do not match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # below occurs if username does not exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # gets the sessions users username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/admin_functions", methods=["GET", "POST"])
def admin_functions():
    if session["user"]:
        return render_template("admin_functions.html")

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # removes user from session cookies
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Tells the app how and where to run application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # ****UPDATE TO "debug=False" PRIOR TO PROJECT SUBMISSION****