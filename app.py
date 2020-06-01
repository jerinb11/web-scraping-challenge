# basic flask server
from flask import Flask, jsonify, render_template, redirect
from scrape_mars import scrape_all
from flask_pymongo import PyMongo 

app = Flask(__name__)

app.config["MONGO_URI"]="mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def home ():
    return "Hello World"


@app.route("/scrape")
def scrape ():
    scrape_data = scrape_all()
    mongo.db.mars_data.update({},scrape_data,upsert=True)
    return redirect('/')

# IF STATEMENT NEEDS TO BE THE LAST THING
if __name__=="__main__":
    app.run(debug=True)

# basic flask server
