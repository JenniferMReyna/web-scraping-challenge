from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app
mongo = PyMongo(app)

@app.route("/")
def index():
    hemis_dictionary = mongo.db.hemis_dictionary.find_one()
    return render_template("index.html", mars = hemis_dictionary)

@app.route("/scrape")
def scrape():
    mar_dicts = mongo.db.mar_dicts
    mars_info = scrape_mars.scrape()
    mar_dicts.update({}, mars_info, upsert = True)
    return redirect("/", code = 302)

if __name__ == "__main__":
    app.run(debug=True)