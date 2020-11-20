from flask import Flask, render_template, request, redirect, url_for, flash
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.environ.get('MONGO_URL')
DB_NAME = "store_manager"

# create the Mongo client
client = pymongo.MongoClient(MONGO_URL)
db = client[DB_NAME]

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def show_homepage():
    all_products = db.product.find()
    return render_template('homepage.template.html',
                           all_products=all_products)


@app.route('/create')
def show_create_product():
    return render_template('create_product.template.html')


@app.route('/create', methods=['POST'])
def process_create_product():
    product_name = request.form.get('product_name')
    product_price = request.form.get('product_price')
    product_desc = request.form.get('product_desc')
    if product_price.isnumeric():
        product_price = float(product_price)

    if len(product_name) == 0:
        flash("Name cannot be empty", "error")
        return render_template('create_product.template.html')

    new_record = {
        'product_name': product_name,
        'product_price': product_price,
        'product_desc': product_desc,
    }

    db.product.insert_one(new_record)
    flash("New product created successful", "success")
    return redirect(url_for('show_homepage'))


@app.route('/edit/<product_id>')
def show_edit_product(product_id):
    product = db.product.find_one({
        '_id': ObjectId(product_id)
    })
    return render_template('edit_product.template.html', product=product)


@app.route('/edit/<product_id>', methods=["POST"])
def process_edit_product(product_id):
    product_name = request.form.get('product_name')
    product_price = float(request.form.get('product_price'))
    product_desc = request.form.get('product_desc')

    db.product.update_one({
        "_id": ObjectId(product_id)
    }, {
        '$set': {
            'product_name': product_name,
            'product_price': product_price,
            'product_desc': product_desc,
        }
    })
    return redirect(url_for('show_homepage'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
