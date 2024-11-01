# Saam Chapter (9)
#Program functions as a financial instistution managment module 
#Module includes 
    #Intrest rate adjustment method
    #Withdraw/deposit methods 
    #balance methods 
    #Intrest calculation method with respect to time 


class BankAcct:
    """
        Class adds bank utilities, allowing Bank Account objects holding:
                -Intrest rate and balance
                
            Methods include:
                - __str__:
                    Prints the current Intrest rate and Balance
                -withdraw:
                    removes specified ammount from the object's balance
                -deposit:
                    adds the specified ammount to the objects balance
                -rate_adjust:
                    replaces current intrest rate with specifed value
                -intrestCalc:
                    calculates intrest for current baalance and specified 
                    ammount of days
                -printIntrest:
                    prints current intrest rate to console
                -printBalance:
                    prints the current balance to the console
                    
                    
    """
    #innitialize class values
    def __init__(self, interest, balance):
        self.interest = interest
        self.balance = balance
        
    #__str__ method for class to return current balance and intrest rate
    def __str__(self):
        return ("The balance is ${}, your interest rate is {}%.".format(self.balance, self.interest))


    #withdraw classmethod 
        #prevent exeptions for overdraft
    def withdraw(self, cash):
        if cash > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            self.balance -= cash
            
    #create deposit method
    def deposit(self, cash):
        self.balance += cash
    
    #Create rate adjustment classmethod
        #replace rate with new rate    
    def rateAdjust(self, rate):
        self.interest = rate
        
    #create intrest calculation classmethod
        #utilize daily intrest x balance x days
    def interestCalc(self, days):
        daily_interest = (self.interest / 365)
        interest = round((daily_interest * self.balance * days), 2)
        print("The interest paid for {} days is ${}".format(days, interest))
        print("----------------------------------")
        self.balance += interest 
        self.printBalance()
    
#Settup print methods for both balance and intrest methods
    
    #prints balance
    def printBalance(self):
        print("Current balance: ${}".format(self.balance))
    
    #prints the intrest rate      
    def printInterest(self):
        print("Current interest rate: {}%".format(self.interest))

        
def main():
    bankAccount = BankAcct(0.05, 100)
    bankAccount.withdraw(100)
    bankAccount.printBalance()
    bankAccount.deposit(35000)
    print(str(bankAccount))
    bankAccount.rateAdjust(.07)
    bankAccount.printInterest()
    bankAccount.interestCalc(13)
    BankAcc
    
main()
        