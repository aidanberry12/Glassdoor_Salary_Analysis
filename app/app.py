# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:11:58 2020

@author: aidan
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('finalized_random_forest_model.pkl', 'rb'))

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
        
    X_dict = {'seniority':0, 'company_rating':0, 'company_size':0, 'company_age':0,
       'role_data analyst':0, 'role_data engineer':0, 'role_data scientist':0,
       'role_director':0, 'role_machine learning engineer':0, 'role_manager':0,
       'role_other':0, 'role_product analyst':0, 'role_research scientist':0,
       'role_software engineer':0, 'sector_Aerospace & Defense':0,
       'sector_Biotech & Pharmaceuticals':0, 'sector_Business Services':0,
       'sector_Education':0, 'sector_Finance':0, 'sector_Government':0,
       'sector_Health Care':0, 'sector_Information Technology':0,
       'sector_Insurance':0, 'sector_Manufacturing':0,
       'sector_Oil, Gas, Energy & Utilities':0, 'sector_Retail':0, 'sector_other':0,
       'region_Midwest':0, 'region_Northeast':0, 'region_South':0, 'region_West':0}
    seniority = request.form['seniority']
    company_rating = request.form['company_rating']
    company_size = request.form['company_size']
    company_age = request.form['company_age']
    title = request.form['title']
    sector = request.form['sector']
    region = request.form['region']
    X_dict['seniority'] = seniority
    X_dict['company_rating']=company_rating
    X_dict['company_size'] = company_size
    X_dict['company_age']=company_age
    X_dict[title] = 1
    X_dict[sector]=1
    X_dict[region]=1
    
   
    final_features = [np.array([*X_dict.values()])]
    prediction = model.predict(final_features)
    
    output = int(prediction[0]*1000)
    return render_template('index.html', prediction_text='Estimated Salary is: $ {:,}'.format(output))
    
@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True, use_reloader = False)