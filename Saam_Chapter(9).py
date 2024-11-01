# Saam Chapter (9):
# Program functions as a financial institution management module 
# Module includes 
# Interest rate adjustment method
# Withdraw/deposit methods 
# Balance methods 
# Interest calculation method with respect to time 

class BankAcct:
    """
    Class adds bank utilities, allowing Bank Account objects holding:
        - Interest rate and balance

    Methods include:
        - __str__:
            Prints the current interest rate and balance
        - withdraw:
            Removes specified amount from the object's balance
        - deposit:
            Adds the specified amount to the object's balance
        - rateAdjust:
            Replaces current interest rate with specified value
        - interestCalc:
            Calculates interest for current balance and specified 
            amount of days
        - printInterest:
            Prints current interest rate to console
        - printBalance:
            Prints the current balance to the console
    """
    # Initialize class values
    def __init__(self, interest, balance):
        self.interest = interest
        self.balance = balance
        
    # __str__ method for class to return current balance and interest rate
    def __str__(self):
        return "The balance is ${}, your interest rate is {}%.".format(self.balance, round(self.interest * 100, 2))

    # Withdraw method 
    def withdraw(self, cash):
        if cash > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            self.balance -= cash
            
    # Deposit method
    def deposit(self, cash):
        self.balance += cash
    
    # Rate adjustment method
    def rateAdjust(self, rate):
        self.interest = rate
        
    # Interest calculation method
    def interestCalc(self, days):
        daily_interest = (self.interest / 365)
        interest = round((daily_interest * self.balance * days), 2)
        interestClean = round(interest * 100, 2)
        print("The interest paid for {} days is ${}".format(days, interestClean))
        print("----------------------------------")
        self.balance += interest 
        self.printBalance()
    
    # Print balance method
    def printBalance(self):
        print("Current balance: ${}".format(self.balance))
    
    # Print interest method      
    def printInterest(self):
        print("Current interest rate: {}%".format(round(self.interest * 100, 2)))

        
def main():
    bankAccount = BankAcct(0.05, 100)
    bankAccount.withdraw(100)
    bankAccount.printBalance()
    bankAccount.deposit(35000)
    print(str(bankAccount))
    bankAccount.rateAdjust(0.07)
    bankAccount.printInterest()
    bankAccount.interestCalc(13)

main()
