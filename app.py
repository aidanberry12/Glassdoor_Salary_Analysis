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
    #print(request.form['title'])
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #print(request.args.get('title'))
    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)

    #output = round(prediction[0], 2)
    seniority = request.form['seniority']
    title = request.form['title']
    sector = request.form['sector']
    region = request.form['region']
    print([seniority, title, sector, region])
    #return render_template('index.html', prediction_text='Estimated Salary is: $ {}'.format(output))
    return render_template('index.html')
@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True, use_reloader = False)