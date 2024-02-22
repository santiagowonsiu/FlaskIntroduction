from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route('/') # return html
def home():
    return render_template('index.html', name = "Tim", age= 20)

@views.route('/profile') # querie parameters
def profile():
    args = request.args
    name = args.get('name')
    return render_template('index.html', name=name)

@views.route('/json') # send json object
def get_json():
    return jsonify({"name": "Tim", "coolness": 10})

@views.route("/data") # get data from an incoming request
def data():
    data = request.json # get data from incoming request
    return jsonify(data) # send data back as json / access

@views.route("go-to-home") # redirect to another route
def go_to_home():
    return redirect(url_for('views.home')) # redirect to home route