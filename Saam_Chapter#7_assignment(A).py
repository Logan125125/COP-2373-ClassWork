# Saam Chapter 7 Assignment A:
    # takes user sentences as input and prints them with running count

#imprt re module for pattern
import re


def main():
    
    #innitialize the count and stop variables
    stop = False
    count = 0
    
    #create a while loop 
        #allows user to input multiple sets of sentences
    while not stop:
        
        check = input('would you like to enter more sentences?').upper()
        

        if check == 'Y':
            
            #takes user input for sentences
                #uses for loop to get count and print each sentence
            s = input("enter sentences below:")
            pat = r'([A-Z][^.!?]*[.!?])'
            sentences = re.findall(pat, s)
            for i in sentences:
                print(i)
                count += 1
            
        elif check == 'N':
            #breaks loop for finish and prints total count
            print(f'there are [{count}] sentences')
            stop = True
        
        # future proofs incorrect answers
        else:
            print('Please enter [y] for yes or [n] for no')
            
if __name__ == "__main__":
    main()
    