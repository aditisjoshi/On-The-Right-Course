# On the Right Course
# Aditi Joshi and Jessica Sutantio
# Software Design Final Project

""" From all of the Olin registaration data, we will be creating a visualization 
displaying the most commong courses taken during a student's Olin career. 
Users will be able to filter the data so that they may visualize the informaiton 
based on major and/ or semester.
"""

import csv
import plotly.plotly as py
from plotly.graph_objs import *
import pandas as pd
import numpy as np

# Name of data file
file_name = 'course_enrollments_2002-2014spring_anonymized.csv'


def course_time(academicStatus,academicYear):
    """
    academicStatus: list denoting freshman, sophomore, junior, and senior status
    academicYear: list denoting semester based off year courses are taken
    returns: course_semester_taken, which is a list of tuples with courseNumbers 
    being paired with the semester they are taken
    """

    # Calculating semester and paring courses with semester
    course_semester_taken = []
    for i in range(len(academicStatus)):
        if (academicStatus[i]=='TF') or (academicStatus[i]=='FF'):
            course_semester_taken.append(1.0)
        elif academicStatus[i]=='FR':
            course_semester_taken.append(1.5)
        elif academicStatus[i]=='SO' and ('FA' in academicYear[i]):
            course_semester_taken.append(2.0)
        elif academicStatus[i]=='SO' and ('SP' in academicYear[i]):
            course_semester_taken.append(2.5)
        elif academicStatus[i]=='JR' and ('FA' in academicYear[i]):
            course_semester_taken.append(3.0)
        elif academicStatus[i]=='JR' and ('SP' in academicYear[i]):
            course_semester_taken.append(3.5)
        elif academicStatus[i]=='SR' and ('FA' in academicYear[i]):
            course_semester_taken.append(4.0)
        elif academicStatus[i]=='SR' and ('SP' in academicYear[i]):
            course_semester_taken.append(4.5)
        else:
            course_semester_taken.append(np.nan)

    return course_semester_taken


def get_df(file_name):
    """
    file_name: csv file that contains the course data
    separates the data from the file into its columns, each column is a list
    returns: df-data frame that holds all the organized data from file_name
    """

    # labelling of data lists
    gradStatus = []
    gradYear = []
    ID = []
    academicYear = []
    gender = []
    academicStatus = []
    major = []
    courseNum = []
    courseSect = []
    courseTitle = []
    professor = []

    # opens csv file and sorts the data into the lists
    with open(file_name, 'rb') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for courseData in data:
            gradStatus.append(courseData[0])
            gradYear.append(courseData[1])
            ID.append(courseData[2])
            academicYear.append(courseData[3])
            gender.append(courseData[4])
            academicStatus.append(courseData[5])
            major.append(courseData[6] + courseData[7]) # includes concentration
            courseNum.append(courseData[8]) # seems to output a ton of spaces after #
            courseSect.append(courseData[9])
            courseTitle.append(courseData[10] + courseData[11]) # includes subtitle
            professor.append(courseData[11])

    semester = course_time(academicStatus,academicYear)

    df = pd.DataFrame({'gradStatus': gradStatus, 'gradYear': gradYear, 'ID': ID, 'academicYear': academicYear, 'gender': gender, 'semester': semester, 'major': major, 'courseNum': courseNum, 'courseSect': courseSect, 'courseTitle': courseTitle, 'professor': professor})

    return df


def capped_percent(df, sem):
    """
    df: data frame that contains all the course registration data as an array
    returns percentage # of ppl in the semester who have taken the 
    course as an ordered list of tuples (courseNum, percentage)
    """

    # # split the dictionary into two lists
    # # sort list of courses by most popular
    # ordered_sem_courses = sorted(sem_courses, key=sem_courses.__getitem__, reverse=True)
    # # make list that contains the number associated with the course
    # percentage = []
    # for course in ordered_sem_courses:
    #     percentage.append(sem_courses[course])

    # capped_sem_courses = ordered_sem_courses[:10]
    # capped_percentages = percentage[:10]

    # return capped_sem_courses, capped_percentages

#################################################### NOT PERCENTAGE YET
    sem_df = df[df.semester==sem]

    """ make a dictionary for each course of grad year and people in that year
    ENGR23434 - {2007:67, 2006: 87, 2010: 0}

    find the number of people registered that semester for each grad year
    gradYear_regist = {2013:89, 2012:97, ...}
    """
 
    numSt = sem_df.ID.nunique()
    # FIND THE COURSES TAKEN IN THE SPECIFIED SEMESTER
    # FIND THE GRADUATION YEAR OF THE PEOPLE WHO TOOK THE COURSE THAT SEM
        # GROUP THOSE PEOPLE
        # DO THE PERCENTAGE CALC WITH THAT GROUP
            # DO IT FOR EVERY GRAD YEAR
    # AVERAGE ALL THOSE PERCENTAGES FOR EVERY COURSE


    # testfile = open('sem1.txt','w')
    # testfile.write(str(sem1))

    return numSt


if __name__ == '__main__':
    # print get_df(file_name)
    print capped_percent(get_df(file_name),1.5)