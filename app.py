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

currentType = ""

@app.route("/")
@app.route("/home")
def home():
    """
    Queries the DB for a list of 'types' which are needed to render the type
    of baked recipes selection boxes displayed on the landing page:
    (index.html).
    """
    types = mongo.db.types.find()
    categories = mongo.db.categories.find()
    return render_template("index.html", types=types, categories=categories)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Login method reflects that taught on the CI Task Manager project.  Checks
    the user login information against the database and returns the correct
    result.
    """
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


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Registration method reflects that taught on the CI Task Manager project.
    Checks the entered registration details for an existing username and email
    before registering user and returning them to the landing page logged in.
    """
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


@app.route("/profile/<username>")
def profile(username):
    """
    Checks user and renders their profile page (My Page).  This function
    reflects that taught on the CI Task Manager project.
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search function for the landing page.  This is a text index on the recipes
    DB in the recipe title and description fields.  Queries database and
    returns recipes contain the search text.
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))

    if len(recipes) <= 0:
        flash(f"No Results found for '{query}'")
        return redirect(url_for("home"))
    else:
        return render_template("recipe_display_search.html", recipes=recipes,
                               query=query)


@app.route("/recipe_display_type/<type>/<type_id>")
def recipe_display_type(type, type_id):
    """
    Queries database and returns recipes that are of the type selected by the
    user on the home page.
    """
    categories = list(mongo.db.categories.find())
    recipes = list(mongo.db.recipes.find({"type": type_id}))

    # takes the id variable and produces another variable which is the
    # type_name
    chosenType = mongo.db.types.find_one({"_id": ObjectId(type_id)})
    typeName = chosenType['type_name']
    # print(typeName)

    if len(recipes) <= 0:
        flash(f"Sorry, we do not have any {type} recipes")
        flash("Do you have any you can share?")
        return redirect(url_for("home"))
    else:
        return render_template("recipe_display_type.html", recipes=recipes,
                               categories=categories, type=type, 
                               type_id=type_id)


@app.route("/recipe_display_category", methods=["GET", "POST"])
def recipe_display_category():
    if request.method == "POST":
        category = request.form.get("cat-search")
        print(category)
        recipes = list(mongo.db.recipes.find({"category": {"$all": [category]}}))
        # recipes = list(mongo.db.recipes.find({"$and": [ {"category": {"$all": [category_id]}}, {"type": type_id}]}))

        print(recipes)
        if len(recipes) <= 0:
            flash(f"Sorry, we do not have any recipes in that category")
            return redirect(url_for("home", username=session["user"]))
        else:
            return render_template("recipe_display_category.html", recipes=recipes)


@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    """
    Queries the database and returns the user selected recipe.
    """
    # Finds selected recipe from database.
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = recipe['category']


    print(categories)
    print(categories[0])
    category1 = categories[0]
    print(category1)
    x = mongo.db.categories.find_one({"_id": ObjectId(category1)})
    print(x)
    category1_name = x['category_name']
    print(category1_name)

    # Gets the user name to display from the stored user id value in the
    # recipe document.
    user_id = recipe['created_by']
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    username = user['username']

    # Gets the ratings list from the database and sets values to variables
    ratings = recipe['ratings']
    number_ratings = len(ratings)

    if number_ratings <= 0:
        rating = 0
    else:
        rating = sum(ratings)//len(ratings)

    reviews = list(mongo.db.reviews.find({"recipe": recipe_id}))
    reviews_count = len(reviews)

    return render_template("view_recipe.html", recipe=recipe,
                        #    category_name=category_name,
                           username=username, rating=rating,
                           number_ratings=number_ratings,
                           reviews=reviews, reviews_count=reviews_count)


@app.route("/user_recipes/<username>")
def user_recipes(username):
    """
    Queries the database and returns the recipes that a user has uploaded.
    """
    # Queries the database for the current user to retrieve the current user id
    # and then assign to a variable.
    current_user = mongo.db.users.find_one({"username": session["user"]})
    user_id = current_user['_id']

    # Retrieves the recipes created by the current user based on the user_id.
    # the variable converted from BSON.ObjectId to a string for the query.
    recipes = list(mongo.db.recipes.find({"created_by": str(user_id)}))

    return render_template("recipe_display_user.html", recipes=recipes,
                           username=username)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Add recipe function.  This method reflects that taught on the CI
    Task Manager project.
    """
    if request.method == "POST":
        current_user = mongo.db.users.find_one({"username": session["user"]})
        user_id = current_user['_id']

        recipe = {
            "recipe_title": request.form.get("recipe-title"),
            "type": request.form.get("recipe-type"),
            "category": request.form.getlist("recipe-category"),
            "description": request.form.get("recipe-description"),
            "prep_time": request.form.get("recipe-preptime"),
            "cook_time": request.form.get("recipe-cooktime"),
            "serves": request.form.get("recipe-serves"),
            "ingredients": request.form.getlist("ingredient"),
            "instructions": request.form.getlist("instruction"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": str(user_id),
            "ratings": []
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your recipe has been added")
        

        return redirect(url_for("profile", username=session["user"]))

    types = mongo.db.types.find()
    categories1 = mongo.db.categories.find()
    categories2 = mongo.db.categories.find()
    categories3 = mongo.db.categories.find()
    return render_template("add_recipe.html", types=types,
                           categories1=categories1, categories2=categories2,
                           categories3=categories3,)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Edit recipe function.  This method reflects that taught on the CI
    Task Manager project.
    """

    if request.method == "POST":
        current_user = mongo.db.users.find_one({"username": session["user"]})
        user_id = current_user['_id']

        # Grabs the current ratings already stored so that they can be
        # re-added with the edit otherwise they would be lost.
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        ratings = recipe['ratings']

        recipe_edit = {
            "recipe_title": request.form.get("recipe-title"),
            "type": request.form.get("recipe-type"),
            "category": request.form.getlist("recipe-category"),
            "description": request.form.get("recipe-description"),
            "prep_time": request.form.get("recipe-preptime"),
            "cook_time": request.form.get("recipe-cooktime"),
            "serves": request.form.get("recipe-serves"),
            "ingredients": request.form.getlist("ingredient"),
            "instructions": request.form.getlist("instruction"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": str(user_id),
            "ratings": ratings
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, recipe_edit)
        flash("Your recipe has been updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    types = mongo.db.types.find()
    categories1 = mongo.db.categories.find()
    categories2 = mongo.db.categories.find()
    categories3 = mongo.db.categories.find()
    category_list = recipe['category']
    category_list_length = len(category_list)
    return render_template("edit_recipe.html", recipe=recipe,
                           types=types, categories1=categories1,
                           categories2=categories2, categories3=categories3,
                           category_list_length=category_list_length,)


@app.route("/rate_recipe/<recipe_id>", methods=["GET", "POST"])
def rate_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if request.method == "POST":
        # Value assigned to variable and converted to an integer from string
        rating = int(request.form.get("rating"))

    mongo.db.recipes.update_one(recipe, {"$push": {"ratings": rating}})
    flash("Rating saved")
    return redirect(url_for("view_recipe", recipe_id=recipe_id))


@app.route("/review_recipe/<recipe_id>/<username>", methods=["GET", "POST"])
def review_recipe(recipe_id, username):
    current_user = mongo.db.users.find_one({"username": session["user"]})
    user_id = current_user['_id']

    if request.method == "POST":
        review = {
            "review": request.form.get("review"),
            "recipe": recipe_id,
            "username": username,
            "user_id": str(user_id)
        }
        mongo.db.reviews.insert_one(review)
        flash("Review saved")

    return redirect(url_for("view_recipe", recipe_id=recipe_id))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Queries the database and deletes the selected recipe.
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for("user_recipes", username=session["user"]))


@app.route("/admin_functions")
def admin_functions():
    """
    Checks user has admin privileges and renders the admin functions page.
    This function reflects that taught on the CI Task Manager project.
    """
    if session["user"]:
        return render_template("admin_functions.html")

    return redirect(url_for("login"))


@app.route("/manage_types/<username>")
def manage_types(username):
    """
    Queries the database and returns the current list of types for the admin
    user to manage.
    """
    types = list(mongo.db.types.find())
    return render_template("admin_type_display.html", types=types,
                           username=username)


@app.route("/manage_categories/<username>")
def manage_categories(username):
    """
    Queries the database and returns the current list of categories for the
    admin user to manage.
    """
    categories = list(mongo.db.categories.find())
    return render_template("admin_category_display.html",
                           categories=categories,
                           username=username)


@app.route("/add_type", methods=["GET", "POST"])
def add_type():
    """
    Add new type function.  This method reflects that taught on the CI Task
    Manager project.
    """
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


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    Add new category function.  This method reflects that taught on the CI Task
    Manager project.
    """
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category-name"),
            "created_by": session["user"]
        }
        mongo.db.categories.insert_one(category)
        flash("New category added")
        return redirect(url_for("manage_categories", username=session["user"]))

    return render_template("add_category.html")


@app.route("/edit_type/<type_id>", methods=["GET", "POST"])
def edit_type(type_id):
    """
    Edit existing type function.  This method reflects that taught on the CI
    Task Manager project.
    """
    if request.method == "POST":
        type_edit = {
            "type_name": request.form.get("type-name"),
            "type_image": request.form.get("type-image"),
            "created_by": session["user"]
        }
        mongo.db.types.update({"_id": ObjectId(type_id)}, type_edit)
        flash("Type updated")
        return redirect(url_for("manage_types", username=session["user"]))

    type = mongo.db.types.find_one({"_id": ObjectId(type_id)})
    return render_template("edit_type.html", type=type)


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    Edit existing category function.  This method reflects that taught on the
    CI Task Manager project.
    """
    if request.method == "POST":
        category_edit = {
            "category_name": request.form.get("category-name"),
            "created_by": session["user"]
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)},
                                   category_edit)
        flash("Category updated")
        return redirect(url_for("manage_categories", username=session["user"]))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_type/<type_id>")
def delete_type(type_id):
    """
    Queries the database and deletes the selected type.
    """
    mongo.db.types.remove({"_id": ObjectId(type_id)})
    flash("Type successfully deleted")
    return redirect(url_for("manage_types", username=session["user"]))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    Queries the database and deletes the selected category.
    """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category successfully deleted")
    return redirect(url_for("manage_categories", username=session["user"]))


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