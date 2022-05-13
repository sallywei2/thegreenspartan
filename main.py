from flask import Flask, render_template, request, Response, stream_with_context

import os

import pandas as pd
import json
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

import sys 
print(sys.version)


# create an instance of Flask

app = Flask(__name__, template_folder='templates')

  
def get_data(country, start_year, end_year):
    df = pd.read_csv("data.csv")
    subset = df[df['country']=country]
    res = subset[(subset['Year']>start_year-1)&(subset['Year']<end_year+1)]
    return res


@app.route('/')
def home():
    return render_template("index.html")
 


@app.route('/visualization', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        #get form data
        country = request.form.get('Country')
        start_year = request.form.get('Start')
        end_year = request.form.get('End')
        
        try:
            data = get_data(country, start_year, end_year)
            result = prediction.to_dict('data')
            return result
        
        except ValueError:
            return "Please enter valid values"
        pass
    
    
    
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
