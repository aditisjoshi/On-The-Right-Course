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
    spamreader = csv.reader(csvfile, delimiter=';',)
    for row in spamreader:
        print ', '.join(row)
