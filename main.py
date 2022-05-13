from flask import Flask, render_template, request, Response, stream_with_context

import os

import pandas as pd
import json
from pandas.core.common import SettingWithCopyWarning
#warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

import sys 
print(sys.version)

# create an instance of Flask

app = Flask(__name__, template_folder='templates')

# to populate country buttons
def list_countries():
	df = pd.read_csv("static/data/data.csv")
	dataset = pd.DataFrame({"country": list(df['country'])})\
		.drop_duplicates()
	countries = dataset['country']
	return countries

DEFAULT_COUNTRY = "Afghanistan"
COUNTRY_LIST = list_countries()

def get_data(country, start_year, end_year):
	df = pd.read_csv("static/data/data.csv")
	subset = df[df["country"] == country]
	result = subset[(subset["Year"]>start_year-1)&(subset['Year']<end_year+1)]

	# return just year and annual temperatures
	dataset = pd.DataFrame({"date": list(result['time']), "value": list(result['Annual'])})
	# remove nulls and format at JSON
	dataset = dataset.where(pd.notnull(dataset), None).to_json()
	return dataset

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method=='POST':
		#get form data
		country = request.form['country'] # read the value of the clicked button
		start_year = 2010 # request.form.get('Start')
		end_year = 2010 #request.form.get('End')
		try:
			data = get_data(country, start_year, end_year)
			return render_template("visualization.html", countries=COUNTRY_LIST, country=country)
		except ValueError:
			pass
	else: # GET method
		return render_template("visualization.html", countries=COUNTRY_LIST, country=DEFAULT_COUNTRY)

@app.route('/visualization', methods = ['POST', 'GET'])
def Visualization():
	if request.method == 'POST':
		pass; #called by home() above instead
	else: # intial GET request to load default data
		country = DEFAULT_COUNTRY
		start_year = 2010 # request.form.get('Start')
		end_year = 2020 #request.form.get('End')
		data = get_data(country, start_year, end_year)
		return data

if __name__ == '__main__':
	app.run(debug=True, threaded=True)
