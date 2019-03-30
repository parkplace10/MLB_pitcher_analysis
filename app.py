import os
import io
import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, redirect, url_for, jsonify, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    
    if request.method == 'POST':
        # read the request data into our variables

        # https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
        # use 'get' if needed
        
        pitcher = request.form['pitcher']
        inning = float(request.form['inning'])
        pscore = float(request.form['pscore'])
        bscore = float(request.form['bscore'])
        outs = float(request.form['outs'])
        balls = float(request.form['balls'])
        strikes = float(request.form['strikes'])
        pitch_num = float(request.form['pitch_num'])
        stance = request.form['stance']
        previous_pitch_type = request.form['previous_pitch_type']
        previous_pitch_location = request.form['previous_pitch_location']

        new = np.array([[pitcher, inning, pscore, bscore, outs, balls, strikes, pitch_num, stance, previous_pitch_type, previous_pitch_location]])

        pitch_type_model = pickle.load(open('models/pitch_type_model.sav', 'rb'))

        pitch_location_model = pickle.load(open('models/pitch_location_model.sav', 'rb'))

        predicted_pitch_type = pitch_type_model.predict(new)
        predicted_pitch_location = pitch_location_model.predict(new)
        
    else:
        # put the default data into our variables
        pitcher = 'Adam Wainwright'
        inning = '1'
        outs = '0'
        balls = '0'
        strikes = '0'
        pitch_num = '1'
        stance = 'R'
        previous_pitch_type = 'Four-Seamer'
        previous_pitch_location = 'middle center'
        predicted_pitch_type = 'Four-Seamer'
        predicted_pitch_location = 'middle center'
        

    input_data = { 'pitcher': pitcher, 'inning': inning, 'outs':outs, 'balls':balls, 'strikes':strikes, 'pitch_num':pitch_num, 'stance':stance, 
    'previous_pitch_type':previous_pitch_type, 'previous_pitch_location': previous_pitch_location}
    output_data = {'predicted pitch type': predicted_pitch_type, 'predicted pitch location': predicted_pitch_location}

    
    return render_template("index-2.html", input_data=input_data, output_data=output_data)

@app.route('/dash')
def dash():

    return render_template("index-3.html")

if __name__ == "__main__":
    app.run(debug=True)
