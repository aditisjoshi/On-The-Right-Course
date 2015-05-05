from flask import render_template, flash, redirect, request
from app import app
from .forms import Inputs
from OnTheRightCourse_dataAnalysis import *

# index view function suppressed for brevity

@app.route('/')
def major_filtering():
    return render_template('login.html', 
                           title='Major Filtering')


@app.route('/filter', methods=['POST'])
def filter():
    major = (request.form['major'])
    semester = (request.form['semester'])
    major_convert = {'ME': 'Mechanical Engineering  ', 'ECE': "Electr'l & Computer Engr", 'E:C': 'Engineering             Computing               ', 'E:Robo': 'Engineering             Robotics                ', 'E:Bio': 'Engineering             Bioengineering          ', 'E:MatSci': 'Engineering             Materials Science       ', 'E:Design': 'Engineering             Design                  ', 'E:Systems': 'Engineering             Systems                 '}
    major = major_convert[major]
    print major
    print semester  
    testFilter = FilterDF(cleanDF, sem=semester, major=major)
    plotThis = testFilter.filter()
    final = RenderDF(plotThis)
    final.render(semester,major)
    path = 'static/'
    if semester:
        image_name = path + 'plot' + semester + '_' + major + '.png'
    else:
        image_name = []
        for i in range(0,7):
            image_name_next = path + 'plot' + str(i) + '_' + major + '.png'
            image_name.append(image_name_next)
    return render_template('filter.html', sem=semester, major=major, image_name=image_name)
