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
    print df
    return df


class CourseDF(objet):
	""" class creates the dataframe that contains the filtering functions """

	
	def dataCleaning(df):
		semLabel(df)
		majorAssignment(df)
		

		def semLabel(academicStatus,academicYear):
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


		def majorAssignment(df):
						"""
		    this method takes in each student's ID and their major. If their major is 
		    undefined at any point, the function will take in the first major it finds
		    for that ID 

		    MAJORS SYNTAX
		     ['Undeclared              ' 
		     'Mechanical Engineering  '
		     'Engineering             '
		     'Undeclared              Systems                 '
		     'Engineering             Systems                 '
		     'Undeclared              Computing               '
		     'Engineering             Computing               '
		     'Undeclared              Materials Science       '
		     'Mechanical Engineering  Materials Science       '
		     'Engineering             Materials Science       '
		     'Mechanical Engineering  Computing               '
		     'Undeclared              Bioengineering          '
		     'Engineering             Bioengineering          '
		     "Electr'l & Computer Engr"
		     'Undeclared              Self Designed           '
		     'Engineering             Self Designed           '
		     'Mechanical Engineering  Bioengineering          '
		     "Electr'l & Computer EngrComputing               "
		     "Electr'l & Computer EngrSystems                 "
		     'Mechanical Engineering  Systems                 '
		     'Mechanical Engineering  Self Designed           '
		     "Electr'l & Computer EngrSelf Designed           "
		     'Undeclared              Design                  '
		     'Mechanical Engineering  Design                  '
		     'Engineering             Design                  '
		     'Undeclared              Robotics                '
		     'Mechanical Engineering  Robotics                '
		     'Engineering             Robotics                '
		     'Exchange Student        Computing               '
		     "Electr'l & Computer EngrRobotics                "]
		    """

		    # all majors that they can list from: ME, ECE, E:C, E:Robo, E:Bio, E:MatSci, E:Design, E:Systems
		    major_convert = {'ME': 'Mechanical Engineering  ', 'ECE': "Electr'l & Computer Engr", 'E:C': 'Engineering             Computing               ', 'E:Robo': 'Engineering             Robotics                ', 'E:Bio': 'Engineering             Bioengineering          ', 'E:MatSci': 'Engineering             Materials Science       ', 'E:Design': 'Engineering             Design                  ', 'E:Systems': 'Engineering             Systems                 '}
		    major = major_convert[major]

		    # finds all the unique ids and all ids
		    uniqueIDs = df.ID.unique()
		    uniquemajors = df.major.unique()

		    # find the start and end indices of the unique IDs 
		    for idNum in uniqueIDs:
		        IDindex = df[df['ID']==idNum].index.tolist()
		        startID = IDindex[0]
		        endID = IDindex[-1]
		        # find the last updated major of the student
		        latestMajor = df['major'][endID]
		        # change all previous majors to be the same as last updated major
		        df.loc[startID:endID+1, 'major'] = latestMajor

        	return df


	def filter(self, sem=none, major=none):


		def semFilter(self,df, sem):
			semCourses = 


		def majorFilter(self,df, major):
			majorDF = self.df[self.df.major == major]

			return majorDF



