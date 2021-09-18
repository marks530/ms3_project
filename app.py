import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
    serviceReports = mongo.db.serviceReports.find()
    return render_template("serviceReports.html", serviceReports = serviceReports)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database collection
        existing_user = mongo.db.serviceDB.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": request.form.get("password")
        }
        mongo.db.serviceDB.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
     port=int(os.environ.get("PORT")), 
     debug=True)
