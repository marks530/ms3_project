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
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
     port=int(os.environ.get("PORT")), 
     debug=True)
