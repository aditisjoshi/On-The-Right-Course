from flask import render_template, flash, redirect, request
from app import app
from .forms import Inputs

# index view function suppressed for brevity

@app.route('/')
def major_filtering():
    return render_template('login.html', 
                           title='Major Filtering')


@app.route('/filter', methods=['POST'])
def filter():
    major = (request.form['major'])
    semester = (request.form['semester'])
    print major
    print semester
    return render_template('filter.html')
