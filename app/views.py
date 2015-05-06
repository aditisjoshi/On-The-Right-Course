from flask import render_template, flash, redirect, request
from app import app
from .forms import Inputs


@app.route('/')
def major_filtering():
    return render_template('login.html', 
                           title='Major Filtering')


@app.route('/filter', methods=['POST'])
def filter():
    # getting user input 
    major = (request.form['major'])
    semester = (request.form['semester'])
    print major
    print semester

    # converting the major input to what can be used in the dictionary
    major_convert = {'ME': 'Mechanical Engineering  ', 'ECE': "Electr'l & Computer Engr", 'E:C': 'Engineering             Computing               ', 'E:Robo': 'Engineering             Robotics                ', 'E:Bio': 'Engineering             Bioengineering          ', 'E:MatSci': 'Engineering             Materials Science       ', 'E:Design': 'Engineering             Design                  ', 'E:Systems': 'Engineering             Systems                 ', 'None': ''}
    major = major_convert[major]

    # getting the picture file names
    path = 'static/'
    if semester == "None":
        semesters = [1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5]
        image1 = path + 'plot' + str(semesters[0]) + '_' + major + '.png'
        image2 = path + 'plot' + str(semesters[1]) + '_' + major + '.png'
        image3 = path + 'plot' + str(semesters[2]) + '_' + major + '.png'
        image4 = path + 'plot' + str(semesters[3]) + '_' + major + '.png'
        image5 = path + 'plot' + str(semesters[4]) + '_' + major + '.png'
        image6 = path + 'plot' + str(semesters[5]) + '_' + major + '.png'
        image7 = path + 'plot' + str(semesters[6]) + '_' + major + '.png'
        image8 = path + 'plot' + str(semesters[7]) + '_' + major + '.png'
        return render_template('filter_allsem.html', sem=semester, major=major, image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6, image7=image7, image8=image8)
    
    else:
        image_name = path + 'plot' + semester + '_' + major + '.png'
        return render_template('filter.html', sem=semester, major=major, image_name=image_name)


@app.route('/refilter', methods=['POST'])
def refilter():
    return render_template('login.html', 
                           title='Major Filtering')
