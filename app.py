from flask import Flask, render_template, request, redirect, url_for, flash
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

# declare the global variables to store the URL to the Mongo database
# and the name of the database that we want to use
MONGO_URL = os.environ.get('MONGO_URL')
DB_NAME = "store_manager"

# create the Mongo client
client = pymongo.MongoClient(MONGO_URL)
# as db variable is outside of every functions, it is a global variable
# we can use the db variable inside any functions
db = client[DB_NAME]

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def show_homepage():
    all_products = db.product.find()
    return render_template('homepage.template.html',
                           all_products=all_products)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
