#Chapter (11): poker assigment
    #Program allows user to play a hand of poker 
    #user may draw five cards and replace as many as neccasary 

#import random module for shuffling
import random

class Deck():
    
    # Initialize deck with given number of decks (default is 1)
    def __init__(self, n_decks=1):
        self.cardList = [num + suit
            for suit in '\u2665\u2666\u2663\u2660'  # Hearts, Diamonds, Clubs, Spades
            for num in 'A23456789TJQK'  # Ace to King
            for deck in range(n_decks)]  # Number of decks
        self.cardsInPlayList = []  # Cards currently dealt
        self.discardsList = []  # Discards pile
        self.cardsDelt = []
        random.shuffle(self.cardList)  # Shuffle deck
        
    # Deal a hand of cards
    def deal(self, numberOfCards):
        n = 0
        self.cardsDelt = []
        # draw a hand as specified by numberOfCards
        while numberOfCards > n:
            
            # Check if the deck is empty and reshuffle 
            if len(self.cardList) < 1:
                random.shuffle(self.discardsList)
                self.cardList = self.discardsList
                self.discardsList = []  # Clear discard pile after reshuffling
                print('Reshuffling!!')
            
            # Deal a card from the deck
            newCard = self.cardList.pop()
            self.cardsDelt.append(newCard)
            n += 1
        return self.cardsDelt
        
    # Start a new hand by moving dealt cards to the discard pile
    def newHand(self):
        self.discardsList += self.cardsInPlayList
        self.cardsInPlayList.clear()

# main function
def main():
    # create stop variable for play loop 
    Stop = False
    deck = Deck()
    
    # create play loop 
    while not Stop:
        # get user input for play
        ask = (input('Would you like to play a hand of poker?: (Y/N)')).upper()
        
        # handle user input for yes and no 
        if ask == 'Y':
            hand = deck.deal(5)
            print(f'your hand: {hand}')
            
            replace = []
            Stop2 = False
            while not Stop2:
                check = (input('would you like to redraw any cards? (y/n)')).upper()
                
                if check == 'Y':
                    check = int(input('which card would you like to replace? (1-5)'))
                    a = deck.deal(1)
                    b = (a[0])
                    hand[(check - 1)] = b  # Replace the selected card
                     
                elif check == 'N':
                    Stop2 = True
                    
                else:
                    print('Please use (y) for yes and (n) for no!')
            print(f'your hand: {hand}')
        elif ask == 'N':
            print('Thanks for playing!')
            Stop = True
        else:
            print('Please use (y) for yes and (n) for no!')
            
main()


                              