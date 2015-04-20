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

    # semester = course_time(academicStatus,academicYear)

    df = pd.DataFrame({'gradStatus': gradStatus, 'gradYear': gradYear, 'ID': ID, 'academicYear': academicYear, 'gender': gender, 'academicStatus': academicStatus, 'major': major, 'courseNum': courseNum, 'courseSect': courseSect, 'courseTitle': courseTitle, 'professor': professor})

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

        # finds all the unique ids and all ids
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

    def dataCleaning(self):
        self.semLabel()
        self.majorAssignment()

        return self.df

######################################################### HAVE NOT IMPLEMENTED BELOW

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

    def semFilter(self):
        """
        Filters the data by a specified semester and outputs a df that 
        contains data for only that semester
        """
        self.df = self.df[self.df.sem == self.sem]

        return self.df

    def majorFilter(self):
        """
        Filters the data by a specified major and outputs a df that 
        contains data for only that major
        """
        self.df = self.df[self.df.major == self.major]

        return self.df

    def filter(self):
        if self.sem not None:
            semFilter()
        if self.major not None:
            majorFilter()

        self.df = capped_percent()

        return self.df

######################################################### HAVE NOT IMPLEMENTED BELOW

    def render():

    def addPercentSymbol():
        """
        takes a list of the percentages and returns a list of the rounded #s with
        the percent symbol
        """

        list_percentages = []
        for element in list_percent:
            list_percentages.append(str(int(element))+'%')

        return list_percentages

    def df_to_list(df):
        """
        takes a dataframe and splits all the columns into separate lists
        """

        df_list = []
        header_list = list(df)
        for header in header_list:
            df_list.append(df[header].tolist())

        return df_lis


    def plot(lists):
        """
        uses plotly to display the appropriate graph
        """
        pass


if __name__ == '__main__':
    df = CourseDF(get_df(file_name))
    print df.dataCleaning().head(20)