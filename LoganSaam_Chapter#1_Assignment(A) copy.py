# Chapter #(1): Project: (A)
#   Ticket POS for cinema ticket presale
#   Limits ticket sales to Four (4) per customer
#   Presale maximum = (20) tickets

import turtle

# Write out number of buyers: (buyer) = funnel for customer count loop
def turtleWriting(buyer):
    t = turtle.Turtle()
    t.hideturtle()
    t.color('white')
    typeface = ("Arial", 25, "bold")
    t.write(f'[{buyer}] customer(s) purchased the available pre-sale tickets', align='center', font=typeface)

# Create screen for ticket Point of Sale (POS)
def screen():
    screen = turtle.Screen()
    screen.title('Ticket Pre-Sale')
    screen.setup(800, 300)
    screen.bgcolor('black')
    return screen

# create code call function to execute ticket sale process
def main():

    # Innit question screen call
    pos = screen()

    # Innit calls for variables
    customer = 0
    tickets = 0

    # Ticket purchase loop until ticket purchase = (20)
    while tickets < 20:
        # Return number of tickets desired
        new_tickets = pos.numinput('Ticket Pre-Sale', 'Enter number of tickets:',
                                1, minval=1, maxval=4)

        # Set True value for tickets
        tickets += new_tickets
        customer +=1

    # Funnel customer count to turtle, writing the message
    turtleWriting(customer)
    #keep screen open for viewing
    turtle.done()

main()