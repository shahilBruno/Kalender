
import time
from flask import Flask, redirect, url_for, render_template
from flask import abort , jsonify
from flask import request	# for the HTTP requests serever make to other 3rd party sites
import requests				# for the HTTP requests client make to our serever
import json					# to work with JSON (javascript object notation)
import csv				# to work with CSV (comma separeted values)
# -----------used flask modules--------------
# Flask
# redirect
# url_for
# render_template
# jsonify

# 	json =========>
# it's basically key value pairs are stored in a mapping like text file and this is file 
# used to store and transmit data. here key is always a string and the pair can be string 
# integer, floating point number or a json object itself.

# 	request =========>
# to make http requests like get, post etc

# 	jsonify =========>
# converts py dicts into json objects

# 	abort =========>
# to raise errors in python flask



#================== INPORTANT NOTES ====================================
# get is an method info transfer between server and database or between client and database
# post is same thing but secure


app = Flask(__name__)


# @app.route('/')		# give my resume. ehich will contain the home link
# def my_page():
# 	return render_template('my_intro.html')


# handling hte http errors=====>
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/data_not_found_404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/internal_server_500.html'), 500

@app.errorhandler(401)
def internal_server_error(error):
    return render_template('errors/wrong_user_401.html'), 500


@app.route('/')
def home():
	# flash('Welcome!')
	return render_template('home/home.html')

@app.route('/<any_text>')		
def render_all_useless_route_to_home(any_text):
	# for safety - all the other invalid routes will be redirested to the home route---------------------
	return redirect(url_for('home'))

@app.route('/signin')
def signin():
	# log-in and sign-in route -------------------------------------------------------------------------
	return render_template('login/login.html', enter_type = 'Signin')

@app.route('/login')
def loin():
	# log-in and sign-in route -------------------------------------------------------------------------
	return render_template('login/login.html', enter_type = 'Login')

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

@app.route('/login_check', methods = ['POST'])
def login_check():
	# gender = request.form(['gender'])
	# country = request.form(['country'])
	user_dict_object = {
		'name': request.form['name'],
		'phn': request.form['phn'],
		'email': request.form['email']
	}

	# adding the login data in 'data/traffic.txt' file
	# with open('data/traffic.txt', 'a') as file:
	# 	user_str = ''
	# 	for user_feature in user:
	# 		user_str += (user_feature + ', ')
	# 	user_str += '\n'
	# 	file.write(user_str)

	### preprocessing the data (python dictionary) is essential - time, contest link, difficulty, cp type or dsa type
	
	# checking the user is signed in or not
	user_info = json.load(open('info/user_info.json', 'r'))
	if user_dict_object in user_info['data']:
		data = json.load(open('cf_data.json', 'r'))
		return render_template('calendar/calendar.html', dict_data=data)
# return str(user)
	else:
		abort(404)

#return redirect(url_for('calendar'))
# ---------------------------------------------------------------------------------------------

@app.route('/get_data', methods = ['GET'])
def get_data():		# get data 2 times a day
	api_url = 'https://codeforces.com/api/contest.list?'
	# api_url = 'https://leetcode.com/contest/weekly-contest-366/'

	response = requests.get(api_url)
	if response.ok:
		json_data = response.json()
		json.dump(json_data, open('cf_data.json', 'w'), indent=4)

		return jsonify({'message': 'JSON data saved successfully'})
	else:
		return render_template('internal_server500.html')

# fro testing something
@app.route('/jsn')
def jsn():
	users = {	'fruit':{"Grapes": "10","color": "green"},
				'vegetable':{"chilli": "4","color": "red"}}
	js = jsonify(users)
	print(type(js))
	print(js)
	return js



# run the server ==============================================================================
if __name__ == '__main__':
	app.run(debug=True)

# path of this file
# cd C:\Users\Admin\Documents\CODES\kalendar_flask
# python main.py
# server environment IP = http://127.0.0.1:5000

