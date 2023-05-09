from flask import Flask, request, render_template
import requests
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'using forex to convert currency'

@app.route('/')
def home_page():
	"""Shows home page with form inputs."""
	return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
	"""Converts currency"""
	
	first_curr = request.form['from']
	second_curr = request.form['to']
	amount = request.form['amount']
	response = requests.get(f'https://api.exchangerate.host/convert?from={first_curr}&to={second_curr}&amount={amount}')
	# response = requests.get('https://api.exchangerate.host/convert?from=USD&to=EUR&amount=100')
	data = response.json()

	# return data
	return json.dumps(data['result'])

	# 1 USD = 0.9100 EUR
	# 100 USD = 91.00 EUR

	# 1 USD = 134.97 JPY
	# 100 USD = 13,495 JPY




