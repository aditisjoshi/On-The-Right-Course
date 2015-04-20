# TEST FILE TO TRY OUT SMALLER FUNCTIONS

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

    # semester = course_time(academicStatus,academicYear)

    df = pd.DataFrame({'gradStatus': gradStatus, 'gradYear': gradYear, 'ID': ID, 'academicYear': academicYear, 'gender': gender, 'academicStatus': academicStatus, 'major': major, 'courseNum': courseNum, 'courseSect': courseSect, 'courseTitle': courseTitle, 'professor': professor})

    return df

class Filter(object):
    """
    end goal is to get the appropriate df from the queried order of filtering
    """

    def __init__(self, df, sem=None, major=None):
        self.df = df
        self.sem = sem
        self.major = major 

    def capped_percent(self):
        """
        NEED TO MAKE SURE THE VALUES OUTPUT IN FULL DF: INCLUDES THE COURSE TITLE
        """

        # counts the number of students registered in specified semester
        # type: integer
        numStudents = self.df.ID.nunique()
        # print 'numStudents',str(numStudents)

        # count the number of people (all gradYears) registered for a course
        # type: series (index is courseNum; value is number of students)
        courseFreq = self.df.groupby('courseNum').ID.nunique()
        # print 'courseFreq',str(courseFreq),str(type(courseFreq))

        # calcs the % by dividing the number of registered students per course by total number of students
        # type: series
        percentages = (courseFreq/numStudents)*100
        
        # sort the Series by highest to lowest percentage
        # type: series
        percentages.sort(ascending=False)

        # limit the list of courses to the top 10
        # type: series
        capped_percentages = percentages.head(10)

        # list of courses
        # type: list
        courses = capped_percentages.index.values.tolist()

        # list of percentages
        # type: list
        list_percent = capped_percentages.tolist()

        # combine them back into a dataframe
        # type: df
        capped_percents = pd.DataFrame({'courseNum': courses, 'Percent': list_percent})

        return capped_percents


if __name__ == '__main__':
    df = Filter(get_df(file_name))
    df.capped_percent().head(20)