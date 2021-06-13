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
    types = mongo.db.types.find()
    return render_template("index.html", types=types)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))

    if len(recipes) <= 0:
        flash(f"No Results found for '{query}'")
        return redirect(url_for("home"))
    else:
        return render_template("recipe_display_search.html", recipes=recipes,
                               query=query)


@app.route("/recipe_display_type/<type>/<id>", methods=["GET", "POST"])
def recipe_display_type(type, id):
    categories = list(mongo.db.categories.find())
    recipes = list(mongo.db.recipes.find({"type": id}))

    # takes the id variable and produces another variable which is the
    # type_name
    chosenType = mongo.db.types.find_one({"_id": ObjectId(id)})
    typeName = chosenType['type_name']
    # print(typeName)

    if len(recipes) <= 0:
        flash(f"Sorry, we do not have any {type} recipes")
        flash("Do you have any you can share?")
        return redirect(url_for("home"))
    else:
        return render_template("recipe_display_type.html", recipes=recipes,
                               categories=categories, type=type)


@app.route("/recipe_display_category/<category>", methods=["GET", "POST"])
def recipe_display_category(category):
    recipes = list(mongo.db.recipes.find({"category": category}))
    if len(recipes) <= 0:
        flash(f"Sorry, we do not have any recipes in that {category}")
        return redirect(url_for("home"))
    else:
        return render_template("recipe_display_category.html", recipes=recipes)


@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", recipe=recipe)


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
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("home", username=session["user"]))
            else:
                # below occurs if passwords do not match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # below occurs if username does not exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_title": request.form.get("recipe-title"),
            "type": request.form.get("recipe-type"),
            "category": request.form.get("recipe-category"),
            "description": request.form.get("recipe-description"),
            "prep_time": request.form.get("recipe-preptime"),
            "cook_time": request.form.get("recipe-cooktime"),
            "serves": request.form.get("recipe-serves"),
            "ingredients": request.form.getlist("ingredient"),
            "instructions": request.form.getlist("instruction"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your recipe has been added")
        return redirect(url_for("profile", username=session["user"]))

    types = mongo.db.types.find()
    categories = mongo.db.categories.find()
    return render_template("add_recipe.html", types=types,
                           categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        recipe_edit = {
            "recipe_title": request.form.get("recipe-title"),
            "type": request.form.get("recipe-type"),
            "category": request.form.get("recipe-category"),
            "description": request.form.get("recipe-description"),
            "prep_time": request.form.get("recipe-preptime"),
            "cook_time": request.form.get("recipe-cooktime"),
            "serves": request.form.get("recipe-serves"),
            "ingredients": request.form.getlist("ingredient"),
            "instructions": request.form.getlist("instruction"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, recipe_edit)
        flash("Your recipe has been updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    types = mongo.db.types.find()
    categories = list(mongo.db.categories.find())
    return render_template("edit_recipe.html", recipe=recipe,
                           types=types, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for("user_recipes", username=session["user"]))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # gets the sessions users username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/user_recipes/<username>", methods=["GET", "POST"])
def user_recipes(username):
    recipes = list(mongo.db.recipes.find({"created_by": username}))
    return render_template("recipe_display_user.html", recipes=recipes,
                           username=username)


@app.route("/manage_types/<username>", methods=["GET", "POST"])
def manage_types(username):
    types = list(mongo.db.types.find())
    return render_template("type_display_admin.html", types=types,
                           username=username)


@app.route("/add_type", methods=["GET", "POST"])
def add_type():
    if request.method == "POST":
        type = {
            "type_name": request.form.get("type-name"),
            "type_image": request.form.get("type-image"),
            "created_by": session["user"]
        }
        mongo.db.types.insert_one(type)
        flash("New type added")
        return redirect(url_for("manage_types", username=session["user"]))

    return render_template("add_type.html")


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
            debug=True)  # **UPDATE TO "debug=False" PRIOR TO PROJECT SUBMISSION**