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
        
    else:
        # put the default data into our variables
        pitcher = 'Adam Wainwright'
        

    # take this input - load the right model based on the pitcher selected
    # feed the rest of the variables into model.predict(...)
    # 

    input_data = { 'pitcher': pitcher }
    output_data = None

    # would probably want to put stuff into dicts
    return render_template("index.html", input_data=input_data, output_data=output_data)


if __name__ == "__main__":
    app.run(debug=True)
