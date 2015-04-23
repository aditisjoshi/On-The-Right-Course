# TEST FILE TO TRY OUT SMALLER FUNCTIONS

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
file_name = 'CourseEnrollmentsFA02-SP15.csv'

def get_df(file_name):
    """
    file_name: csv file that contains the course data
    separates the data from the file into its columns, each column is a list
    returns: df-data frame that holds all the organized data from file_name
    """

    # labelling of data lists
    ID = []
    academicYear = []
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
            ID.append(courseData[0])
            academicYear.append(courseData[1])
            academicStatus.append(courseData[2])
            major.append(courseData[3] + courseData[4]) # includes concentration
            courseNum.append(courseData[5]) # seems to output a ton of spaces after #
            courseSect.append(courseData[6])
            courseTitle.append(courseData[7] + courseData[8]) # includes subtitle
            professor.append(courseData[9])

    # semester = course_time(academicStatus,academicYear)

    df = pd.DataFrame({'ID': ID, 'academicYear': academicYear, 'academicStatus': academicStatus, 'major': major, 'courseNum': courseNum, 'courseSect': courseSect, 'courseTitle': courseTitle, 'professor': professor})

    return df

class CourseDF(object):
    """ 
    class creates the dataframe that contains the cleaning and 
    filtering functions
    """

    def __init__(self, df):
        self.df = df

    def semLabel(self):
        """
        takes the df and goes row by row to determine the semester the
        course was registered for
        returns: df that has the semesters labeled from 1-4.5
        """
       
        # relabeling semester row by row
        for i in range(len(self.df.index)):
            status = self.df.loc[i,'academicStatus']
            year = self.df.loc[i,'academicYear']
            if (status=='TF') or (status=='FF'):
                sem = 1.0
                # print sem
            elif status=='FR':
                sem = 1.5
            elif status=='SO' and ('FA' in year):
                sem = 2.0
            elif status=='SO' and ('SP' in year):
                sem = 2.5
            elif status=='JR' and ('FA' in year):
                sem = 3.0
            elif status=='JR' and ('SP' in year):
                sem = 3.5
            elif status=='SR' and ('FA' in year):
                sem = 4.0
            elif status=='SR' and ('SP' in year):
                sem = 4.5
            else:
                sem = np.nan

            # overwrite the academicStatus to use our numbering convention (1-4.5)
            self.df.loc[i,'academicStatus'] = sem

        return self.df

    def majorAssignment(self):
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

        # # all majors that they can list from: ME, ECE, E:C, E:Robo, E:Bio, E:MatSci, E:Design, E:Systems
        # major_convert = {'ME': 'Mechanical Engineering  ', 'ECE': "Electr'l & Computer Engr", 'E:C': 'Engineering             Computing               ', 'E:Robo': 'Engineering             Robotics                ', 'E:Bio': 'Engineering             Bioengineering          ', 'E:MatSci': 'Engineering             Materials Science       ', 'E:Design': 'Engineering             Design                  ', 'E:Systems': 'Engineering             Systems                 '}
        # major = major_convert[self.df.col.major]

        # finds all the unique ids of all ids
        uniqueIDs = self.df.ID.unique()
        uniquemajors = self.df.major.unique()

        # find the start and end indices of the unique IDs 
        for idNum in uniqueIDs:
            IDindex = self.df[self.df['ID']==idNum].index.tolist()
            startID = IDindex[0]
            endID = IDindex[-1]
            # find the last updated major of the student
            latestMajor = self.df['major'][endID]
            # change all previous majors to be the same as last updated major
            self.df.loc[startID:endID+1, 'major'] = latestMajor

        return self.df

    def oldCourses(self):
        """ Get rid of courses that are no longer offered from the df by
        looking at courses that are only offered in the last 4 years
        """
        # STILL NEED TO IMPLEMENT

        pass

    def courseNames(self):
        """
        make courses of the same courseNum have the first courseTitle assciated
        with it
        """

        # start dictionary that pairs courseNum with courseTitle
        NumTitlePair = {}
        # find all the unique courseNums and put
        uniqueCourseNum = self.df.courseNum.unique()
        # print uniqueCourseNum
        for i in range(len(self.df.index)):
            if self.df.courseNum[i] in NumTitlePair:
                self.df.courseTitle[i] = NumTitlePair[self.df.courseNum[i]]
            else:
                NumTitlePair[self.df.courseNum[i]] = self.df.courseTitle[i]

        print NumTitlePair

        return self.df

    def dataCleaning(self):
        self.semLabel()
        self.majorAssignment()
        self.courseNames()

        return self.df


if __name__ == '__main__':
    data = CourseDF(get_df(file_name))
    cleanDF = data.dataCleaning().head(10)
    print cleanDF