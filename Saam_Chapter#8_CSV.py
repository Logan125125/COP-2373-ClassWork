# Saam Chapter(8) assignment CSV:
    #create a program to read and write a student grade dictionary

import csv


#open read / write function
def readWrite():
    #ask if user wants to read or write
    answer = input("would you like to read or write grades? (R/W/Quit):").upper()
    
    #send user to requested function
    if answer == 'R':
        readGrades()
        
    elif answer == 'W':
        writeGrades()
    
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
    with open('grades.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = Header)
        
        writer.writeheader()
        writer.writerows(gradesList)
    readWrite()

def readGrades():
    dash = ('-'* 20)
    with open('grades.csv') as grades:
        grades = csv.DictReader(grades)
        for row in grades:
            print(row)
            print(dash)
    readWrite()
    
    


    
if __name__ == "__main__":
    readWrite()


