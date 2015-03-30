# On the Right Course
# Aditi Joshi and Jessica Sutantio
# Software Design Final Project

""" From all of the Olin registaration data, we will be creating a visualization 
displaying the most commong courses taken during a student's Olin career. 
Users will be able to filter the data so that they may visualize the informaiton 
based on major and/ or semester.
"""

import csv
with open('course_enrollments_2002-2014spring_anonymized.csv', 'rb') as csvfile:
    courseData = csv.reader(csvfile, delimiter=';',)
    gradStatus = courseData[0]
	gradYear = courseData[1]
	ID = courseData[2]
	gender = courseData[3]
	academicStatus = courseData[4]
	major = courseData[5] + courseData[6]
	courseNum = courseData[7]
	courseSect = [8]
	courseTitle = [9] + courseData[10]
	professor = [11]

print courseTitle


#########################################################################
# Labelling
