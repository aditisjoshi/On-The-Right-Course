from flask import render_template, flash, redirect, request
from app import app
from .forms import Inputs
#   

# index view function suppressed for brevity

@app.route('/')
def major_filtering():
    return render_template('login.html', 
                           title='Major Filtering')


@app.route('/filter', methods=['POST'])
def filter():
    major = (request.form['major'])
    semester = (request.form['semester'])
    major_convert = {'ME': 'Mechanical Engineering  ', 'ECE': "Electr'l & Computer Engr", 'E:C': 'Engineering             Computing               ', 'E:Robo': 'Engineering             Robotics                ', 'E:Bio': 'Engineering             Bioengineering          ', 'E:MatSci': 'Engineering             Materials Science       ', 'E:Design': 'Engineering             Design                  ', 'E:Systems': 'Engineering             Systems                 ', 'None': ''}
    major = major_convert[major]
    path = 'static/'
    if semester is None:
        image_name = path + 'plot' + semester + '_' + major + '.png'
    else:
        image_name = []
        semesters = [1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5]
        for semester in semesters:
            image_name_next = path + 'plot' + str(semester) + '_' + major + '.png'
            image_name.append(image_name_next)
        print image_name
    return render_template('filter.html', sem=semester, major=major, image_name=image_name)


@app.route('/refilter', methods=['POST'])
def refilter():
    return render_template('login.html', 
                           title='Major Filtering')
