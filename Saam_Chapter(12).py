 #Saam Chapter(12) assignment:
    # annalyze the grades.csv from chapter 8 assignment A

import csv
import numpy as np


#open read / write function
def readWrite():
    #ask if user wants to read or write
    answer = input("would you like to read, write, or average grades? (R/W/A/Quit):").upper()
    
    #send user to requested function
    if answer == 'R':
        readGrades()
        
    elif answer == 'W':
        writeGrades()
    
    elif answer == 'A':
        gradeAverages()
    
    elif answer == 'QUIT':
        None
    
    #for all answers other than requested recall function
    else:
        readWrite()
        

def writeGrades():
    # Initialize grades list and header
    gradesList = []
    Header = ['First Name',
                'Last Name',
                'Test (1) Grade',
                'Test (2) Grade',
                'Test (3) Grade']
    
    # Ask for the number of students
    numberStudent = int(input('How many grades would you like to enter? '))
    
    for _ in range(numberStudent):
        studentInfo = {
                    'First Name': input('Enter First Name: '),
                    'Last Name': input('Enter Last Name: '),
                    'Test (1) Grade': input('Enter Test (1) Grade: '),
                    'Test (2) Grade': input('Enter Test (2) Grade: '),
                    'Test (3) Grade': input('Enter Test (3) Grade: ')
                    }
        
        #append instance of student information
        gradesList.append(studentInfo) 
        
    #open grades file, create if it doesent exist
    with open('grades.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = Header)
        
        #write header if new file
        #append grades to grades.csv
        writer.writeheader()
        writer.writerows(gradesList)
        
    #loop back to read write quit choice
    readWrite()

# allow user to read grades.csv
def readGrades():
    
    #create break variable
    dash = ('-'* 20)
    
    #open the grades.csv fie to read grades
    with open('grades.csv') as grades:
        grades = csv.DictReader(grades)
        for row in grades:
            #print each row from file
            print(row)
            
            #break up instances of grades
            print(dash)
    #loop back to read write quit choice
    readWrite()



def gradeAverages():

    #create break variable
    dash = ('-'* 20)

    # Read grades from the CSV file
    #obtain just grades and convert to int

    gradeArray = np.loadtxt('grades.csv', dtype='S10', delimiter=',')
    gradeArray = np.delete(gradeArray,[0,1], axis=1)
    gradeArray = np.delete(gradeArray,[0], axis = 0)
    gradeArray = gradeArray.astype(np.int32)
    print()
    print(dash)
    print()

    #get total mean, median, standard deviation, min, max

    print('The mean of all three exams is: ', np.mean(gradeArray))
    print('The median of all three exams is: ', np.median(gradeArray))
    print('The standard deviation of all three exams is: ', np.std(gradeArray))
    print('The minimum value of all three exams is: ', np.max(gradeArray))
    print('The maximum value of all three exams is: ', np.min(gradeArray))

    #specify test one Grades, mean, median, standard deviation, min, max

    testOne = np.delete(gradeArray,[1,2], axis=1)
    print('The mean of testOne is: ', np.mean(testOne))
    print('The median of testOne is: ', np.median(testOne))
    print('The standard deviation of testOne is: ', round(np.std(testOne), 2))
    print('The minimum value of testOne is: ', np.min(testOne))
    print('The maximum value of testOne is: ', np.max(testOne))
    print()
    print(dash)
    print()

    #specify test two grades

    testTwo = np.delete(gradeArray,[0,2], axis=1)
    print('The mean of testTwo is: ', np.mean(testTwo))
    print('The median of testTwo is: ', np.median(testTwo))
    print('The standard deviation of testTwo is: ', round(np.std(testTwo), 2))
    print('The minimum value of testTwo is: ', np.min(testTwo))
    print('The maximum value of testTwo is: ', np.max(testTwo))
    print()
    print(dash)
    print()

    #specify test three grades
    testThree = np.delete(gradeArray,[0,1], axis=1)
    print('The mean of testThree is: ', np.mean(testThree))
    print('The median of testThree is: ', np.median(testThree))
    print('The standard deviation of testThree is: ', round(np.std(testThree), 2))
    print('The minimum value of testThree is: ', np.min(testThree))
    print('The maximum value of testThree is: ', np.max(testThree))
    print()
    print(dash)
    print()

    # specify a passing grade value
    passGrade = 60

    #find pass percentage
    students = gradeArray.shape[0]
    passedCourse = np.all(gradeArray >= passGrade, axis=1)
    passPercent = round(((np.sum(passedCourse) /students) * 100), 2)

    #print pass percent
    print(f" {passPercent} % of the class passed the course")

    #print students who passed per test
    print(f"{np.sum(testOne >= passGrade)} students passed testOne")
    print(f"{np.sum(testTwo >= passGrade)} students passed testTwo")
    print(f"{np.sum(testThree >= passGrade)} students passed testThree")
    print()
    print(dash)
    print()

    #loop back to read or write
    readWrite()



if __name__ == "__main__":
    readWrite()
#Calculate and print the following statistics for each exam (columns):
    #Mean (average)
    #Median
    #Standard deviation
    #Minimum
    #Maximum
#Calculate and print the overall statistics for the entire dataset (all exams combined):
    #Mean (average) grade across all exams 
    #Median grade across all exams 
    #Standard deviation of grades across all exams 
    #Minimum grade across all exams 
    #Maximum grade across all exams 
#Determine and print the number of students who passed and failed each exam. Consider a passing grade as 60 or above.
#Calculate and print the overall pass percentage across all exams.

