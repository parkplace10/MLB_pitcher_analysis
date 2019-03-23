import os
import io
import numpy as np

from flask import Flask, request, redirect, url_for, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        # read the request data into our variables

        # https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
        # use 'get' if needed
        pitcher = request.form['pitcher']
        inning = int(request.form['inning'])
        outs = int(request.form['outs'])
        balls = int(request.form['balls'])
        strikes = int(request.form['strikes'])
        stance = request.form['stance']
        first = request.form['first']
        second = request.form['second']
        third = request.form['third']
        pitch_type = ""
        pitch_location = ""

        
    else:
        # put the default data into our variables
        pitcher = 'Adam Wainwright'
        pitch_type = 'Four-Seamer'
        pitch_location = 'middle center'
        

    # take this input - load the right model based on the pitcher selected
    # feed the rest of the variables into model.predict(...)
    # 

    input_data = { 'pitcher': pitcher} #'inning': inning, 'outs':outs, 'balls':balls, 'strikes':strikes, 
    #'stance':stance, 'first':first, 'second':second, 'third':third
    output_data = None #{'pitch type': pitch_type, 'pitch location': pitch_location}

    # would probably want to put stuff into dicts
    return render_template("index.html", input_data=input_data, output_data=output_data)


if __name__ == "__main__":
    app.run(debug=True)
