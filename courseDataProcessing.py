# On the Right Course
# Aditi Joshi and Jessica Sutantio
# Software Design Final Project

""" From all of the Olin registaration data, we will be creating a visualization 
displaying the most commong courses taken during a student's Olin career. 
Users will be able to filter the data so that they may visualize the informaiton 
based on major and/ or semester.
"""

import csv

# Name of data file
file_name = 'course_enrollments_2002-2014spring_anonymized.csv'

def get_data_as_lists(file_name):
    """
    separates the data from the file into its columns, each column is a list
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

    return gradStatus, gradYear, ID, academicYear, gender, academicStatus, major, courseNum, courseSect, courseTitle, professor


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
        if academicStatus[i] == 'TF' or academicStatus[i] == 'FF':
            course_semester_taken.append((courseNum[i],1.0))
        elif academicStatus[i]=='FR':
            course_semester_taken.append((courseNum[i],1.5))
        elif academicStatus[i]=='SO' and ('FA' in academicYear[i]):
            course_semester_taken.append((courseNum[i],2.0))
        elif academicStatus[i]=='SO' and ('SP' in academicYear[i]):
            course_semester_taken.append((courseNum[i],2.5))
        elif academicStatus[i]=='JR' and ('FA' in academicYear[i]):
            course_semester_taken.append((courseNum[i],3.0))
        elif academicStatus[i]=='JR' and ('SP' in academicYear[i]):
            course_semester_taken.append((courseNum[i],3.5))
        elif academicStatus[i]=='SR' and ('FA' in academicYear[i]):
            course_semester_taken.append((courseNum[i],4.0))
        elif academicStatus[i]=='SR' and ('SP' in academicYear[i]):
            course_semester_taken.append((courseNum[i],4.5))

    return course_semester_taken


def semester_dict(course_semester_taken, sem_number):
    """ 
    returns the courses taken in a certain semester along with their
    frequency taken
    """

    sem_courses = {}
    for element in course_semester_taken:
        if element[1] == sem_number:
            course = element[0]
            count = sem_courses.get(course,0)
            sem_courses[course] = count + 1

    return sem_courses


if __name__ == '__main__':
    
    gradStatus, gradYear, ID, academicYear, gender, academicStatus, major, courseNum, courseSect, courseTitle, professor = get_data_as_lists(file_name)

    print semester_dict(course_time(academicStatus,academicYear),1.0)
    print len(semester_dict(course_time(academicStatus,academicYear),1.0))
    print len(ID)