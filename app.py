from flask import Flask, request, render_template, flash, redirect
from currency_symbols import CurrencySymbols
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
	symbol = CurrencySymbols.get_symbol(second_curr)
	response = requests.get(f'https://api.exchangerate.host/convert?from={first_curr}&to={second_curr}&amount={amount}&places=2')

	data = response.json()
	result = json.dumps(data['result'])

	errors = []
	if len(first_curr) != 3 or first_curr != first_curr.upper() or first_curr[0] == first_curr[1]:
		errors.append(f"Not valid code: {first_curr}")
	if len(second_curr) != 3 or second_curr != second_curr.upper() or second_curr[0] == second_curr[1]:
		errors.append(f"Not valid code: {second_curr}")
	try:
		float(amount)
	except ValueError:
		errors.append(f"Not valid amount: {amount}")
	
	if errors:
		for error in errors:
			flash(error, 'error')
		return redirect('/')
	else:
		return render_template('result.html', result=result, symbol=symbol)

		

	# 1 USD = 0.9100 EUR
	# 100 USD = 91.00 EUR

	# 1 USD = 134.97 JPY
	# 100 USD = 13,495 JPY

	


