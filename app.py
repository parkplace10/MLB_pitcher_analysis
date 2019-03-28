import os
import io
import numpy as np
from flask import Flask, request, redirect, url_for, jsonify, render_template
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func


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
        first = request.form['first']
        second = request.form['second']
        third = request.form['third']
        previous_pitch_type = ""
        previous_pitch_location = ""

        # new = np.array(['outs', 'balls', ''strikes])

        # model.predict(new)
        
    else:
        # put the default data into our variables
        pitcher = 'Adam Wainwright'
        pitch_type = 'Four-Seamer'
        pitch_location = 'middle center'
        

    # take this input - load the right model based on the pitcher selected
    # feed the rest of the variables into model.predict(...)
    # 

    input_data = { 'pitcher': pitcher, 'inning': inning, 'outs':outs, 'balls':balls, 'strikes':strikes, 
    'pitch_num':pitch_num, 'stance':stance, 'first':first, 'second':second, 'third':third}
    output_data = None #{'pitch type': pitch_type, 'pitch location': pitch_location}

    # would probably want to put stuff into dicts
    return render_template("index-2.html", input_data=input_data, output_data=output_data)


if __name__ == "__main__":
    app.run(debug=True)
