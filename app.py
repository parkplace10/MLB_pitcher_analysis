import os
import io
import numpy as np
import pandas as pd
import pickle
import sklearn
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
        pitchnum = float(request.form['pitchnum'])
        stance = request.form['stance']
        typeloc = request.form['typeloc']
        previous_pitch_type = request.form['previous_pitch_type']
        previous_pitch_location = request.form['previous_pitch_location']

        new = np.array([[pitcher, inning, pscore, bscore, outs, balls, strikes, pitchnum, stance, typeloc, previous_pitch_type, previous_pitch_location]])

        pitch_type_model = pickle.load(open('models/pitch_type_model.sav', 'rb'))
        pitch_location_model = pickle.load(open('models/pitch_location_model.sav', 'rb'))

        predicted_pitch_type = pitch_type_model.predict(new)
        predicted_pitch_location = pitch_location_model.predict(new)
        
    else:
        # put the default data into our variables
        pitcher = '1'
        inning = '1'
        outs = '0'
        balls = '0'
        strikes = '0'
        pitchnum = '1'
        stance = '1'
        typeloc = '1'
        pscore = '1'
        bscore = '1'
        previous_pitch_type = '1'
        previous_pitch_location = '1'
        predicted_pitch_type = '1'
        predicted_pitch_location = '1'
        

    input_data = { 'pitcher': pitcher, 'inning': inning, 'outs':outs, 'balls':balls, 'strikes':strikes, 'pitchnum':pitchnum, 'stance':stance, 'typeloc':typeloc, 'pscore':pscore, 'bscore':bscore, 'previous_pitch_type':previous_pitch_type, 'previous_pitch_location': previous_pitch_location}
    output_data = {'predicted pitch type': predicted_pitch_type, 'predicted pitch location': predicted_pitch_location}

    
    return render_template("index.html", input_data=input_data, output_data=output_data)

@app.route('/dash')
def dash():

    return render_template("index-3.html")

if __name__ == "__main__":
    app.run(debug=True)
