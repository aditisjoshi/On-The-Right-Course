# On the Right Course
# Aditi Joshi and Jessica Sutantio
# Software Design Final Project

""" From all of the Olin registaration data, we will be creating a visualization 
displaying the most commong courses taken during a student's Olin career. 
Users will be able to filter the data so that they may visualize the informaiton 
based on major and/ or semester.
"""

import csv

def get_data_as_lists(file_name):

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

    with open(file_name, 'rb') as csvfile:
        data = csv.reader(csvfile, delimiter=';',)
        for courseData in data:
            gradStatus.append(courseData[0])
            gradYear.append(courseData[1])
            ID.append(courseData[2])
            academicYear.append(courseData[3])
            gender.append(courseData[4])
            academicStatus.append(courseData[5])
            major.append(courseData[6] + courseData[7])
            courseNum.append(courseData[8])
            courseSect.append(courseData[9])
            courseTitle.append(courseData[10] + courseData[11])
            professor.append(courseData[11])

    return courseNum


def course_time(academicStatus,academicYear):
    """
    academicStatus: list denoting freshman, sophomore, junior, and senior status
    academicYear: list denoting semester based off year courses are taken
    returns: course_time, which is a dictionary of courseNumbers being paired with
        the semester they are taken
    """

    # Calculating semester
    semester = []
    for i in range(len(academicStatus)):
        if academicStatus[i] in ('FF', 'TF'):
            #1.0
        if academicStatus[i]=='FR':
            #1.5
        if academicStatus[i]=='SO' and ('FA' in academicYear[i]):
            #2.0
        if academicStatus[i]=='SO' and ('SP' in academicYear[i]):
            #2.5
        if academicStatus[i]=='JR' and ('FA' in academicYear[i]):
            #3.0
        if academicStatus[i]=='JR' and ('SP' in academicYear[i]):
            #3.5
        if academicStatus[i]=='SR' and ('FA' in academicYear[i]):
            #4.0
        if academicStatus[i]=='JR' and ('SP' in academicYear[i]):
            #4.5

    # Pairing course with semester
    course_time = {}
    for i in range(len(semester)):
        course_time[courseNum[i]] = semester[i]
        # course_time will always be overidden
        # course_time = {[ENGR0000,1.0],[ENGR0000,3.0]....}
        # does not count frequency

def count_frequency(courseList):
    d = dict()
    for item in courseList:
        current = d.get(item,0)
        d[item] = current + 1
    return d

if __name__ == '__main__':
    courseNum = get_data_as_lists('course_enrollments_2002-2014spring_anonymized.csv')
    print count_frequency(courseNum)