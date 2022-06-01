
class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
def balance():
    balance = 5000
    print("your balance is", balance)

def withdrawal():
    balance=5000
    amount=int(input("enter the amount you want to withdraw: "))
    currentBalance= balance - amount
  
    if(amount>balance):
        print("you do not have sufficient money in your bank account")
        print("you have",+balance ,"in your bank account")
        withdrawal()
    elif(amount==balance, amount<balance):
          print("you have withdrawn", amount)
          print("your current balance is ", currentBalance)
    

def takeCard():
    cardNumber = input("enter your card number: ")
    
    letterCount=0
    for letter in cardNumber:
        letterCount=letterCount+1
    if(letterCount>2 or letterCount<2):
        print("card number is invalid. Please enter a valid card number")
        takeCard()
    else:
        takePin()
        
    

def takePin():
    pin = input("enter your pin: ")
    letter1Count=0
    for letter in pin:
        letter1Count=letter1Count+1

    if(letter1Count>3 or letter1Count<3):
        print("pin number is invalid. Please enter a valid pin number")
        takePin()
    else:
        whatToDo()


def whatToDo():
    print("what do you want to do? ")
    print("1.Balance  2.Withdrawl")
    activity = int(input("enter activity number :- "))

    if(activity == 1):
        balance()
    elif(activity==2):
        withdrawal()
    else:
        print("please enter correct number")
        whatToDo()


takeCard()



