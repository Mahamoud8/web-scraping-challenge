# Import dependencies
from flask import Flask, render_template, redirect
from scrape_mars import scrape
import pymongo

# Flask
app = Flask(__name__)
app.config["Mongo_URI"] = "mongodb://localhost:27017/db"
mongo = PyMongo(app)

@app.route("/")
def index(): 
    mars_info = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info = mars_info)

@app.route("/scrape")
def scrape(): 
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_image()
    mars_data = scrape_mars.scrape_mars_facts()
    mars_data = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)
    
    
