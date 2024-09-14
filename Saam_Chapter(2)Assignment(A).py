# Assignment A Chapter 2
# Create an email spam filter 
# filter out 3 spam words and predict if an email is spam

def main():
    
    #create spam validation dictionary
    # 30 spam words to filter against
    filter = [
    "free",
    "win",
    "prize",
    "cash",
    "urgent",
    "money",
    "guarantee", 
    "offer",
    "save",
    "instant",
    "click",
    "buy",
    "now",
    "limited",
    "risk-free",
    "reward",
    "exclusive",
    "secret",
    "investment",
    "winner",
    "earn",
    "cheap",
    "spam",
    "credit",
    "debt",
    "cancel",
    "claim",
    "online",
    "trial",
    "unsecured"
]
    # create spam score host variable
    spam_score = (0)
    
    # create blank dictioonary to conctenate spam to
    spam_words = []
    
    # get email from user
    # conctenate a space to allow split method around spacs
    email = (' ' + input("Enter Email "))
    
    #lower whole email to eliminate case base errors 
    # and split email into list of str's
    email = (email.lower()).split()
    
    #for each word (string) in the email 
    # test against spam filter add to score and list if spam
    for str in email:
        if str in filter:
            spam_score += 1
            spam_words.append(str)
            
    #Print out messages based on spam score, spam words, and likely hood of spam
    print('The spam score is: ', spam_score)
    if spam_score > 0:
        print('The spam words used are: ', spam_words)
    if spam_score > 5:
        print('This is a spam message')
    else:
        print('This email is likely safe')

if __name__ == "__main__":
    main()
