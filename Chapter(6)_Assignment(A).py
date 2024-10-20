#Chapter (6) Assignment (A):
#Checks validity of the phone number
#zipcode and social security number entered 
#by the user then prints results

#import re for use of regular statements to check
import re

#create phone number check function
def phoneCheck(phone):
    pattern = r'\d{3}[ -]\d{3}[ -]\d{4}'
    verified = False
    
    #check phone number against regular statment 
    if re.fullmatch(pattern, phone):
        verified = True

    return verified

#create zip check function
def zipCheck(zipcode):
    pattern = r'\d{5}'
    patternFull = r'\d{5}[ -]\d{4}'
    verified = False
    
    #check zip against regular statment 
    if re.fullmatch(pattern, zipcode):
        verified = True
    elif re.fullmatch(patternFull, zipcode):
        verified = True

    return verified

#create zip check function
def socialCheck(social):
    pattern = r'\d{3}[ -]\d{2}[ -]\d{4}'
    verified = False
    
    #Checks zip against regular statment 
    if re.fullmatch(pattern, social):
        verified = True

    return verified

#define the main function
def main():
    
    #get user input for phone, zip, and social 
    #run input directly through check funtions
        #creates set of Boolean validity vars
    phoneValid = phoneCheck(input('Enter a Phone Number: '))
    zipValid = zipCheck(input('Enter a Zip Code: '))
    socialValid = socialCheck(input('Enter a Social Security Number: '))
    
    #utilize boolean if true to automaticaly print true/ false statments
    if phoneValid:
        print('The Phone Number Entered is Correct')
    else:
        print("An Invalid Phone was Entered")
    if zipValid:
        print('The Zip Code Entered is Correct')
    else:
        print("An Invalid Zip Code was Entered")
    if socialValid:
        print('The Social Security Number Entered is Correct')
    else:
        print("An Invalid Social Security Number was Entered")
        
# only run if main file allowing import of check functions
if __name__ == "__main__":
    main()
