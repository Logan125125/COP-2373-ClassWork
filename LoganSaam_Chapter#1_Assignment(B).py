# Project (b) chapter #(2):
# Program reads list of magic 8 ball epressions
# using  random pakckage display a random respoinse
    
# Import randint to generate random response
from random import randint

# create random number (1-12) and return int
def random():
    return randint(1, 12)
    
# read line from response file a return str
def readline(line_number):
    try:
        with open('8ball_responses.txt', 'r') as file:
            lines = file.readlines()
        # Adjust for zero-based index
        return lines[line_number - 1].strip()  # Remove newline character
    except IndexError:
        return "Response not found."
    except FileNotFoundError:
        return "Response file not found."
    
# generate a random number and use it to read response line
# then display text line 
def main():
    # Create count for while function
    count = (0)
    
    #create a repetition while loop for continal use
    while count < 1:
        
        print('')
        print("Ask a question and the magic will guide you!")
        print('')
        useranswer =input(str('would you me to answer a question? (y/n): ')).strip()
        
        # fix error of lowercae input
        useranswer = useranswer.upper()
        
        # adds line break for clarit
        # reads and displays 8 ball        
        if useranswer == 'Y':
            print('')
            print(readline(random()))
        
        # adds a break line for clarity
        # breaks code to execute no command
        elif useranswer == 'N':
            print('')
            print('Goodbye!')    
            count = 1
        
        # adds a line break for clarity                
        # repeat for answers out of scope
        else:
            print('')
            print('Please enter (y/n) to continue or quit: ')
            
        
# prevent calling of main function if imported to another script
if __name__ == "__main__":
    main()
    