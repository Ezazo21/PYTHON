win=69
chances=9
while chances>0:
    guess=int(input("Guess the number :"))
    if guess==win:
        print("Congrats!!You win")
        print("The number of guesses you took to win =",chances)
    elif guess>win:
        print("Your number is greater than the winning number")
        chances-=1
        print("Try again")
        print("Chances left",chances)
    elif guess<win:
        print("Your number is less than the winning number")
        chances-=1
        print("Try again")
        print("Chances left",chances)
print("You lost")