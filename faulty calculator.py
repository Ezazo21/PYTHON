win=69
chances=9
while chances>0:
    guess=int(input("Guess the number"))
    if guess==win:
        print("You win")
    else :
        chances-=1
        print("Try again")
        print("Chances left",chances)
print("You lost")