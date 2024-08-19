import random
cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
dealer=[]
user=[]

def dealer_card():
    card_d = random.choice(cards)
    dealer.append(card_d)


def user_card (): 
    card_u= random.choice(cards)
    user.append(card_u)


def picking_cards():
    for _ in range(2):
        dealer_card()
        user_card()
    print("ther dealer cards are: ")
    print(dealer)
    print("the user cards are : ")
    print(user)

#game start 

print("ur hands are ")

picking_cards()

def user_turn():
    yes = True
    while yes == True:
        hint_or_stand=int(input('do u wanna hint or stand ?? (1 for hint / 2 for stand ): '))
        if hint_or_stand == 1:
            user_card()
            print("ur hand now is : ")
            print(user)
            total=sum(user)
            print(total)
            if total > 21 :
                print("you lost")
                yes = False
        elif hint_or_stand == 2 :
            print("u stands")
            total = sum(user)
            print(user)
            print(total)
            yes= False
            if total > 21 :
                print("you lost")
                yes = False
                total = 0
    return total

def dealer_turn():
    dealer_choice = [True , False]
    yes = 1
    while yes == 1:
        he_choose = random.choice(dealer_choice) # true means that he choosed to hint
        if he_choose == True :
            dealer_card()
            print("dealer hand now is : ")
            print(dealer)
            totald=sum(dealer)
            print(totald)
            if totald > 21 :
                print("dealer lost cuz  have more than 21 ")
                totald =0
                yes = 2
            else :
                continue 

        elif he_choose == False : #false means thate he choosed to stands 
            print(" dealer stands")
            totald = sum(dealer)
            print(dealer)
            print(totald)
            if (totald > 21) or (totald<17) :
                print("dealer lost cuz  have less than 17")
                totald =0
                yes = 2
            else :
                continue
                
    return totald   

#compring to get the winner 


total = user_turn()
totald= dealer_turn()

if total > totald :
    print("user win")
elif total == totald:
    print("dealer win")
else:
    print("dealer win")

    

