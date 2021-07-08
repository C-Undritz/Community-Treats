import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_paginate import Pagination, get_page_args
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# Creates an instance of Flask stored in variable 'app'.
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# ---------- Global functions: ----------
def find_user():
    """
    Determines current user using the username value of the current session
    user and returns the current user as a dict.
    """
    current_user = mongo.db.users.find_one({"username": session["user"]})
    return current_user


def find_id():
    """
    Determines the ObjectId value of the current user and returns it as a
    string value.
    """
    user_id = str(find_user()['_id'])
    return user_id


def get_recipes(recipes, offset=0, per_page=5):
    return recipes[offset: offset + per_page]


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login'))
    return wrap
# ---------------------------------------


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
            "password": generate_password_hash(request.form.get("password")),
            "admin": False
        }
        mongo.db.users.insert_one(register)

        # put new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        # return render_template("index.html")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/profile/<username>")
@login_required
def profile(username):
    """
    Checks user and renders their profile page (My Page).  This function
    reflects that taught on the CI Task Manager project.
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        current_user = mongo.db.users.find_one({"username": session["user"]})
        admin = current_user['admin']

        return render_template("profile.html", username=username, admin=admin)

    return redirect(url_for("login"))


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
@login_required
def edit_profile(username):
    """
    Allows user to view and update profile details.
    """
    current_user = find_user()
    user_id = find_id()

    if request.method == "POST":
        admin = current_user['admin']
        password = current_user['password']

        if (current_user['fname'] == request.form.get("fname").lower()):
            updated_fname = current_user['fname']
        else:
            updated_fname = request.form.get("fname").lower()

        if (current_user['lname'] == request.form.get("lname").lower()):
            updated_lname = current_user['lname']
        else:
            updated_lname = request.form.get("lname").lower()

        if (current_user['email'] == request.form.get("email").lower()):
            updated_email = current_user['email']
        else:
            updated_email = request.form.get("email").lower()

        if (current_user['username'] == request.form.get("username").lower()):
            updated_username = current_user['username']
        else:
            updated_username = request.form.get("username").lower()

        profile_update = {
            "fname": updated_fname,
            "lname": updated_lname,
            "email": updated_email,
            "username": updated_username,
            "password": password,
            "admin": admin
        }

        mongo.db.users.update({"_id": ObjectId(user_id)}, profile_update)
        session["user"] = request.form.get("username").lower()
        flash("Profile updated")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("edit_profile.html",
                           current_user=current_user)


@app.route("/edit_password/<username>", methods=["GET", "POST"])
@login_required
def edit_password(username):
    """
    Allows user to change their password.  This function first deletes the
    existing password field entirely before re-inserting it with the new
    password along with the current user details.
    """
    current_user = find_user()
    user_id = find_id()

    if request.method == "POST":
        mongo.db.users.update({"_id": ObjectId(user_id)}, {"$unset": {"password": ""}})

        password_update = {
            "fname": current_user['fname'],
            "lname": current_user['lname'],
            "email": current_user['email'],
            "username": current_user['username'],
            "password": generate_password_hash(request.form.get("password")),
            "admin": current_user['admin']
        }

        mongo.db.users.update({"_id": ObjectId(user_id)}, password_update)
        flash("Password updated")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("edit_password.html",
                           current_user=current_user)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search function for the landing page.  This is a text index on the recipes
    DB in the recipe title and description fields.  Queries database and
    returns recipes contain the search text.
    """
    if request.method == "POST":
        query = request.form.get("query")
        recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))

        if len(recipes) <= 0:
            flash(f"No Results found for '{query}'")
            return redirect(url_for("home"))
        else:
            return render_template("recipe_display_search.html",
                                   recipes=recipes,
                                   query=query, navigation=5)


@app.route("/recipe_display_type/<type>/<type_id>")
def recipe_display_type(type, type_id):
    """
    Queries database and returns recipes that are of the type selected by the
    user on the home page.
    """
    categories = list(mongo.db.categories.find())
    recipes = list(mongo.db.recipes.find({"type": type_id}))

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(recipes)

    paginated_recipes = get_recipes(recipes)
    pagination = Pagination(page=page, per_page=per_page, total=total)

    if len(recipes) <= 0:
        flash(f"Sorry, we do not have any {type} recipes")
        return redirect(url_for("home"))
    else:
        return render_template("recipe_display_type.html", recipes=paginated_recipes,
                               categories=categories, type=type,
                               pagination=pagination,
                               type_id=type_id, navigation=1)


@app.route("/recipe_display_category/<type_id>/<type>", methods=["GET",
                                                                 "POST"])
def recipe_display_category(type_id, type):
    """
    Allows the user to display recipes of a 'type' by any of the categories
    that are associated with the recipe.  Function first guards against errors
    by checking for a Nonetype that would result from the user clicking the
    search button without first selecting a value.
    """
    if request.method == "POST":
        search = request.form.get("cat-search")
        if search is None:
            return redirect(url_for("recipe_display_type", type=type,
                                    type_id=type_id))
        else:
            category = mongo.db.categories.find_one({"_id": ObjectId(search)})
            recipes = list(mongo.db.recipes.find({"$and": [
                                                 {"category":
                                                  {"$all": [search]}},
                                                   {"type": type_id}]}))

            category_name = category['category_name']

            if len(recipes) <= 0:
                flash("Sorry, there are no recipes in that category")
                return redirect(url_for("recipe_display_type", type=type,
                                        type_id=type_id))
            else:
                return render_template("recipe_display_category.html",
                                       recipes=recipes, type=type,
                                       type_id=type_id, navigation=2,
                                       category_name=category_name)


@app.route("/view_recipe/<recipe_id>/<navigation>")
def view_recipe(recipe_id, navigation):
    """
    Queries the database and returns the user selected recipe.
    """
    # Finds selected recipe from database.
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # Deals with 'unclassified' type recipes so they still display.
    recipe_type_id = recipe['type']
    if recipe_type_id == "unclassified":
        recipe_type_name = "unclassified"
    else:
        recipe_type = mongo.db.types.find_one({"_id": ObjectId(recipe_type_id)})
        recipe_type_name = recipe_type['type_name']

    # Extracts recipe category values, cross references them with the
    # 'categories' collection to get the category names, puts them in
    # a list which is then formatted to be displayed with the recipe.
    categories = recipe['category']
    categories_list = []
    for i in range(len(categories)):
        category_doc = mongo.db.categories.find_one(
            {"_id": ObjectId(categories[i])})
        category_name = category_doc['category_name']
        categories_list.append(str(category_name))

    def format_list(list):
        return str(list).replace('[', '').replace(']', '').replace(',', ' /').replace('\'', '')

    recipe_categories = (format_list(categories_list))

    # Gets the recipe authors name to display from the stored 'created_by' id
    # value in the recipe document.
    author_id = recipe['created_by']
    author = mongo.db.users.find_one({"_id": ObjectId(author_id)})
    author_name = author['username']

    # Gets the ratings count setting it to a variable.
    number_ratings = len(recipe['ratings'])

    # Gets the reviews and reviews count setting both to variables.
    reviews = list(mongo.db.reviews.find({"recipe": recipe_id}))
    reviews_count = len(reviews)

    if 'user' in session:
        user_id = find_id()

        # Determines if recipe being viewed has already been reviewed by
        # current user
        if mongo.db.reviews.find_one({"$and": [{"user_id": user_id},
                                               {"recipe": recipe_id}]}):
            reviewed = True
        else:
            reviewed = False

        # Determines if recipe being viewed is already stored as a favourite
        # for the current user
        if mongo.db.favourites.find_one({"$and": [
                                        {"user": user_id},
                                        {"recipe_id": recipe_id}]}):
            favourite = True
        else:
            favourite = False

    else:
        reviewed = False
        favourite = False

    return render_template("view_recipe.html", recipe=recipe,
                           type=recipe_type_name,
                           type_id=recipe_type_id,
                           recipe_categories=recipe_categories,
                           author_name=author_name,
                           number_ratings=number_ratings,
                           reviews=reviews, reviews_count=reviews_count,
                           reviewed=reviewed, favourite=favourite,
                           navigation=navigation)


@app.route("/user_recipes/<username>")
@login_required
def user_recipes(username):
    """
    Queries the database and returns the recipes that a user has uploaded.
    """
    user_id = find_id()

    # Retrieves the users recipes based on the user_id.
    recipes = list(mongo.db.recipes.find({"created_by": user_id}))

    return render_template("recipe_display_user.html", recipes=recipes,
                           username=username, navigation=3)


@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    """
    Add recipe function.  This method reflects that taught on the CI
    Task Manager project.
    """
    if request.method == "POST":
        user_id = find_id()

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
            "created_by": user_id,
            "ratings": [],
            "rating": 0
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your recipe has been added")

        return redirect(url_for("profile", username=session["user"]))

    types = mongo.db.types.find()
    categories1 = mongo.db.categories.find()
    categories2 = mongo.db.categories.find()
    categories3 = mongo.db.categories.find()
    return render_template("add_recipe.html", types=types,
                           categories1=categories1,
                           categories2=categories2,
                           categories3=categories3,)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    """
    Edit recipe function.  This method reflects that taught on the CI
    Task Manager project.
    """
    if request.method == "POST":
        user_id = find_id()

        # Grabs the current ratings and rating already stored so that they can
        # be re-added with the edit otherwise they would be lost.
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        ratings = recipe['ratings']
        rating = recipe['rating']

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
            "created_by": user_id,
            "ratings": ratings,
            "rating": rating
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
                           categories2=categories2,
                           categories3=categories3,
                           category_list_length=category_list_length,)


@app.route("/delete_recipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def delete_recipe(recipe_id):
    """
    Queries the database and deletes the selected recipe.  Also deletes any
    associated reviews and favourites to keep the database clean.
    """
    if request.method == "POST":
        # Deletes reviews associated with the recipe.
        mongo.db.reviews.delete_many({"recipe": recipe_id})

        # Deletes favourites associated with the recipe.
        mongo.db.favourites.delete_many({"recipe_id": recipe_id})

        # Removes recipe
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        flash("Recipe successfully deleted")

        return redirect(url_for("user_recipes", username=session["user"]))


@app.route("/rate_recipe/<recipe_id>/<navigation>", methods=["GET", "POST"])
def rate_recipe(recipe_id, navigation):
    """
    Posts the rating selected by the user to the database where it is saved
    on the recipe document as a string.  This value is used to work out an
    overall rating that is saved as a single integer saved also on the
    recipe document.
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if request.method == "POST":
        # Value assigned to variable and converted to an integer from string
        new_rating = int(request.form.get("rating"))

        mongo.db.recipes.update_one(recipe, {"$push": {"ratings": new_rating}})

        overall_rating = round((sum(recipe['ratings']) + new_rating) /
                              ((len(recipe['ratings'])) + 1))
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
                                    {"$set": {"rating": overall_rating}})
        flash("Rating saved")

    return redirect(url_for("view_recipe", recipe_id=recipe_id,
                            navigation=navigation))


@app.route("/review_recipe/<recipe_id>/<username>/<navigation>", methods=["GET", "POST"])
@login_required
def review_recipe(recipe_id, username, navigation):
    """
    Checks whether the current user has already reviewed the recipe and if so
    informs them as such.  If no review then saves the review along with user
    and recipe information into a separate collection.
    """
    user_id = find_id()

    if mongo.db.reviews.find_one({"$and": [{"user_id": user_id},
                                           {"recipe": recipe_id}]}):
        flash("You have already reviewed this recipe")
    else:
        if request.method == "POST":
            review = {
                "review": request.form.get("review"),
                "recipe": recipe_id,
                "username": username,
                "user_id": user_id
            }
            mongo.db.reviews.insert_one(review)
            flash("Review saved")

    return redirect(url_for("view_recipe", recipe_id=recipe_id,
                            navigation=navigation))


@app.route("/add_favourite/<recipe_id>/<user>/<navigation>", methods=["GET", "POST"])
@login_required
def add_favourite(recipe_id, user, navigation):
    """
    Adds recipe to the users favourites.  Function determines user_id and
    recipe title from parameters passed to the function.
    """
    user_id = find_id()

    if mongo.db.favourites.find_one({"$and": [
                                    {"user": user_id},
                                    {"recipe_id": recipe_id}]}):
        flash("This recipe is already saved as a favourite")
    else:
        if request.method == "POST":
            recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
            recipe_title = recipe['recipe_title']

            favourite = {
                "recipe_id": recipe_id,
                "recipe_title": recipe_title,
                "user": user_id
            }

            mongo.db.favourites.insert_one(favourite)
            flash("Saved to your favourites")

    return redirect(url_for("view_recipe", recipe_id=recipe_id,
                            navigation=navigation))


@app.route("/remove_favourite/<recipe_id>/<user>/<navigation>", methods=["GET", "POST"])
@login_required
def remove_favourite(recipe_id, user, navigation):
    """
    Queries the database and removes the recipe from the users favourites.
    """
    user_id = find_id()

    if request.method == "POST":
        remove = mongo.db.favourites.find_one({"$and": [
            {"user": user_id}, {"recipe_id": recipe_id}]})
        mongo.db.favourites.remove(remove)
        flash("Recipe removed from favourites")

    return redirect(url_for("view_recipe", recipe_id=recipe_id,
                            navigation=navigation))


@app.route("/favourite_recipes/<username>")
@login_required
def favourite_recipes(username):
    """
    Queries the database and returns the recipes that a user has marked and
    favourites.
    """
    user_id = find_id()

    # Retrieves the favourites documents created by the current user based on
    # the user_id.  The variable converted from BSON.ObjectId to a string for
    # the query.
    favourites = list(mongo.db.favourites.find({"user": user_id}))

    return render_template("recipe_display_favourites.html",
                           favourites=favourites,
                           username=username,
                           navigation=4)


@app.route("/admin_functions")
@login_required
def admin_functions():
    """
    Checks user has admin privileges and renders the admin functions page.
    This function reflects that taught on the CI Task Manager project.
    """
    return render_template("admin_functions.html")


@app.route("/manage_types/<username>")
@login_required
def manage_types(username):
    """
    Queries the database and returns the current list of types for the admin
    user to manage.
    """
    types = list(mongo.db.types.find())
    return render_template("admin_type_display.html", types=types,
                           username=username)


@app.route("/manage_categories/<username>")
@login_required
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
@login_required
def add_type():
    """
    Add new type function.  This method reflects that taught on the CI Task
    Manager project.
    """
    if request.method == "POST":
        existing_type = mongo.db.types.find_one(
            {"type_name": request.form.get("type-name").lower()})
        if existing_type:
            flash("Type already exists")
            return redirect(url_for("add_type"))

        type = {
            "type_name": request.form.get("type-name").lower(),
            "type_image": request.form.get("type-image"),
            "created_by": session["user"]
        }
        mongo.db.types.insert_one(type)
        flash("New type added")
        return redirect(url_for("manage_types", username=session["user"]))

    return render_template("add_type.html")


@app.route("/add_category", methods=["GET", "POST"])
@login_required
def add_category():
    """
    Add new category function.  This method reflects that taught on the CI Task
    Manager project.
    """
    if request.method == "POST":
        existing_category = mongo.db.categories.find_one(
            {"category_name": request.form.get("category-name").lower()})
        if existing_category:
            flash("Category already exists")
            return redirect(url_for("add_category"))

        category = {
            "category_name": request.form.get("category-name").lower(),
            "created_by": session["user"]
        }
        mongo.db.categories.insert_one(category)
        flash("New category added")
        return redirect(url_for("manage_categories", username=session["user"]))

    return render_template("add_category.html")


@app.route("/edit_type/<type_id>", methods=["GET", "POST"])
@login_required
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
@login_required
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


@app.route("/delete_type/<type_id>", methods=["GET", "POST"])
@login_required
def delete_type(type_id):
    """
    Queries the database and deletes the selected type.  Also updates the
    recorded 'type' of any recipes that are classified under the deleted
    type, to 'unclassified'
    """
    if request.method == "POST":
        # Removes type.
        mongo.db.types.remove({"_id": ObjectId(type_id)})

        # Updates the type of affected recipes to 'unclassified'
        mongo.db.recipes.update_many({"type": type_id},
                                     {"$set": {"type": "unclassified"}})

        flash("Type successfully deleted")
        return redirect(url_for("manage_types", username=session["user"]))


@app.route("/delete_category/<category_id>", methods=["GET", "POST"])
@login_required
def delete_category(category_id):
    """
    Queries the database and deletes the selected category.  Also removes
    the deleted category from the categories array on each recipe in the
    database.
    """
    if request.method == "POST":
        # Removes the category reference from the recipes category array
        mongo.db.recipes.update_many({ }, {"$pull": {"category": category_id}})

        # Removes category.
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("Category successfully deleted")
        return redirect(url_for("manage_categories", username=session["user"]))


@app.route("/create_admin/<username>", methods=["GET", "POST"])
@login_required
def create_admin(username):
    """
    Create admin function mirrors the registration function, but is accessed by
    an existing admin user to create the role and applies a value of 'true' to
    the database document field of 'admin'.
    """
    if request.method == "POST":
        # checks the database for existing user
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("create_admin"))
        elif existing_email:
            flash("Email already exists")
            return redirect(url_for("create_admin"))

        role = {
            "fname": request.form.get("fname").lower(),
            "lname": request.form.get("lname").lower(),
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "admin": True
        }
        mongo.db.users.insert_one(role)

        flash("Admin role created")
        return redirect(url_for("admin_functions", username=session["user"]))

    return render_template("create_admin.html", username=username)


@app.route("/logout")
@login_required
def logout():
    # removes user from session cookies
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500


# Tells the app how and where to run application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # **UPDATE TO "debug=False" PRIOR TO PROJECT SUBMISSION**

