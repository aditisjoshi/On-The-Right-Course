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

######################################################### CURRENTLY IMPLEMENTING

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
        takes in the semester filtered df and outputs the top ten percentages in a df
        
        1. find the number of uniqueIDs
        2. find how many unique students are taking the course per semester (series)
        3. convert the values of the series into percentages (still tied to courses)
        4. sort those percentages from hight to low
        5. cap at top ten
        6. put series back into a df by: 
        courses be the index
        other columns contain: courseNum, courseTitle, section, 

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

        # return self.df

    def semFilter(self):
        """
        Filters the data by a specified semester and outputs a df that 
        contains data for only that semester
        returns modified df that only contains info for that specified 
        semester
        """
        self.df = self.df[self.df.sem == self.sem]

        return self.df

    def majorFilter(self):
        """
        Filters the data by a specified major and outputs a df that 
        contains data for only that major
        returns modified df that only contains info for that specified 
        semester
        """
        self.df = self.df[self.df.major == self.major]

        return self.df

    def output8Sem(self):
        """
        For scenarios (no filter or only majorFilter) in which all 8 sem are displayed,
        run through semFilter and capped_percent for each sem
        return all 8 sem in 8 separate dfs compiled into a list
        """
        
        semList = [1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5]
        dfList = []

        for element in semList:
            self.sem = element
            semFilter()
            # capped_percent()
            dfList.append(self.df)

        return dfList

    def filter(self):
        # filtered by sem and major at the same time
        if self.sem != None and self.major != None:
            semFilter()
            majorFilter()
            capped_percentages()
            return self.df
        # filtered by semester only
        elif self.sem != None:
            semFilter()
            capped_percentages()
            return self.df
        # filtered by major only
        elif self.major != None:
            eightDFs = output8Sem()
            filteredEightDFs = []
            # go thru the list of dfs and filter major
            for singleDF in eightDFs:
                self.df = singleDF
                majorFilter()
                capped_percent()
                filteredEightDFs.append(self.df)
            return filteredEightDFs
        # no filter
        else:
            eightDFs = output8Sem()
            filteredEightDFs = []
            for singleDF in eightDFs:
                self.df = singleDF
                capped_percent()
                filteredEightDFs.append(self.df)
            return filteredEightDFs

######################################################### HAVE NOT IMPLEMENTED BELOW


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

    def render():
        for dataFrame in self.df:
            percent_text = addPercentSymbol(dataFrame)
            plot_this = df_to_list(dataFrame)
            url = plot(plot_this)


if __name__ == '__main__':
    df = CourseDF(get_df(file_name))
    print df.dataCleaning().head(20)