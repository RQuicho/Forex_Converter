from flask import Flask, request
import requests

url = 'https://api.exchangerate.host/convert?from=USD&to=EUR'
response = requests.get(url)
data = response.json()

print(data)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'using forex to convert currency'

@app.route('/')
def home_page():
	"""Shows home page with form inputs."""
	from_input = request.args['firstCurrency']
	to_input = request.args['secondCurrency']
