from bottle import Bottle, route, get, post, template, request, static_file
from pymongo import MongoClient
from bson.json_util import dumps
import json

client = MongoClient('mongodb://heroku_j47rhw75:2ctpo13v9ptj497mqf7q1o1aps@ds151909.mlab.com:51909/heroku_j47rhw75')
db = client.heroku_j47rhw75

app = Bottle(__name__)

@app.route('/')
def root():
	return 'Hello!'

@app.route('/hello')
def new_hello():
	name = request.GET.get('name')

	return 'Hello '+str(name)

@app.route('/hello/<name>')
def hello(name):
	return 'Hello '+name

@app.route('/fetch_file')
def fetch_file():
	return static_file('style.css', root='./')

@app.route('/temp')
def temp_test():
	return template("<h1>{{name}}</h1>", {"name":"OCL"})

@app.route('/getData')
def getData():
	cur = db.aug10.find()
	data = json.loads(dumps(cur))

	# return {'data': data}

	return template("<p>ID: {{id}}</p><p>Type: {{user_type}}</p>", {'id': data[0]['user_id'], 'user_type': data[0]['type']})