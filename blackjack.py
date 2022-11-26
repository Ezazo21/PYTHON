import random
card=[1,2,3,4,5,6,7,8,9,10,10,10,10]
def youwantotplay():
    global f
    f=input("Do you want to play blackjack? (y/n) :")
def player_card():
    global a
    global b
    global c
    global second_card
    a=card[random.randint(0,len(card)-1)]
    b=card[random.randint(0,len(card)-1)]
    print(f"Your cards are {a},{b}")
    c=card[random.randint(0,len(card)-1)]
    print(f"Computer card {c}")
    second_card=card[random.randint(0,len(card)-1)]
def want_more():
    global e
    e=-1
    d=input("You want one more card (y/n): ")
    if d=="y":
        e=card[random.randint(0,len(card)-1)]
        print(f"Your third card is {e}")
youwantotplay()
while f=="y" or f=="Y":
    print('''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\               
      `------'                           |__/           ''')
    player_card()
    want_more()
    if e!=-1:
        player_cards=a+b+e
        if player_cards>21:
            print("You Lose")
        elif player_cards<(c+second_card):
            print(f"computer cards :{c},{second_card}")
            print(f"Your cards :{a},{b},{e}")
            print("You lose")
        elif player_cards>(c+second_card):  
            print(f"computer cards :{c},{second_card}")
            print(f"Your cards :{a},{b},{e}")
            print("You win")
        else:
            print(f"computer cards :{c},{second_card}")
            print(f"Your cards :{a},{b},{e}")
            print("Draw")
    else:
        player_cards=a+b
        if player_cards>21:
            print("You Lose")
        elif player_cards<(c+second_card):
            print(f"computer cards :{c},{second_card}")
            print(f"Your cards :{a},{b}")
            print("You lose")
        elif player_cards>(c+second_card): 
            print(f"computer cards :{c},{second_card}")
            print(f"Your cards :{a},{b}")
            print("You win")
        else:
            print(f"computer cards :{c},{second_card}")
            print(f"Your cards :{a},{b}")
            print("Draw")
    youwantotplay()
if f=="n" or f=="N":
    print("Thanks for running !!")
else:
    print("Not valid input!!")