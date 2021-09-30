import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")  # get the database name
app.config["MONGO_URI"] = os.environ.get("MONGO_URI") # Mongo database connection string
app.secret_key = os.environ.get("SECRET_KEY") # key is required when using some of the functions from Flask 

mongo = PyMongo(app)

@app.route("/") 
@app.route("/get_serviceReports")
def get_serviceReports():
    serviceReports = list(mongo.db.serviceReports.find())
    return render_template("serviceReports.html", serviceReports = serviceReports)

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    serviceReports = list(mongo.db.serviceReports.find({"$text": {"$search": query}}))
    return render_template("serviceReports.html", serviceReports = serviceReports)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database collection
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        confirm_password = request.form.get("confirm_password")    

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "employee_type": request.form.get("employee_type")
        }
        if request.form.get("password") == request.form.get("confirm_password"):
            mongo.db.users.insert_one(register)
            flash("Registration Successful!")
            # return user to login page after registration
            return redirect(url_for("login")) 

        else:
            flash("Registration unSuccessful!")
        # return user to register page after unsuccessful registration
    return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET","POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)
    
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/add_record", methods=["GET","POST"])
def add_record():
    if request.method == "POST":
        is_resolved = "Yes" if request.form.get("is_resolved") else "No"
        report = {
            "engineer_name": request.form.get("username"),
            "customer_name": request.form.get("customer_name"),
            "date_received": request.form.get("date_received"),
            "machine_type": request.form.get("machine_type"),
            "fault_description": request.form.get("fault_description"),
            "action_taken": request.form.get("action_taken"),
            "parts_used": request.form.get("parts_used"),
            "is_resolved": request.form.get("is_resolved")

        }
        mongo.db.serviceReports.insert_one(report)
        flash("Record Successfully Added")
        return redirect(url_for("get_serviceReports"))
    usernames = mongo.db.users.find().sort("username", 1)
    return render_template("add_record.html", usernames=usernames)

@app.route("/edit_record/<serviceReport_id>", methods=["GET", "POST"])
def edit_record(serviceReport_id):
    if request.method == "POST":
        is_resolved = "Yes" if request.form.get("is_resolved") else "No"
        submit= {
            "engineer_name": request.form.get("engineer_name"),
            "customer_name": request.form.get("customer_name"),
            "date_received": request.form.get("date_received"),
            "machine_type": request.form.get("machine_type"),
            "fault_description": request.form.get("fault_description"),
            "action_taken": request.form.get("action_taken"),
            "parts_used": request.form.get("parts_used"),
            "is_resolved": request.form.get("is_resolved")

        }
        mongo.db.serviceReports.update({"_id": ObjectId(serviceReport_id)}, submit)
        flash("Record Successfully Updated")

    serviceReport = mongo.db.serviceReports.find_one({"_id": ObjectId(serviceReport_id)})
    serviceReports = list(mongo.db.serviceReports.find())
    return render_template("edit_record.html", serviceReport=serviceReport, serviceReports = serviceReports)

@app.route("/delete_record/<serviceReport_id>")
def delete_record(serviceReport_id):
    mongo.db.serviceReports.remove({"_id": ObjectId(serviceReport_id)})
    flash("Record Successfully Deleted")
    return redirect(url_for("get_serviceReports"))

@app.route("/manage_users")
def manage_users():
    users = list(mongo.db.users.find().sort("username", 1))
    return render_template("manage_users.html", users=users)

@app.route("/manage_passwords")
def manage_passwords():
    passwords = list(mongo.db.users.find().sort("password"))
    return render_template("manage_passwords.html", passwords=passwords)

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        user = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password")),
            "employee_type": request.form.get("employee_type")
        }
        mongo.db.users.insert_one(user)
        flash("New User Added")
        return redirect(url_for("manage_users"))
               
    return render_template("add_user.html")


@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if request.method == "POST":
        submit = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get ("password")),
            "employee_type": request.form.get("employee_type")
        }
        mongo.db.users.update({"_id": ObjectId(user_id)}, submit)
        flash("User Successfully Updated")
        return redirect(url_for("manage_users"))

    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("edit_user.html", user=user)

@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("User Removed Successfully")
    return redirect(url_for("manage_users"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
     port=int(os.environ.get("PORT")), 
     debug=True)
