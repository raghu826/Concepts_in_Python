import random
number = random.randrange(1,101)


i = 0
while i <= 100:

    guess = int(input("guess the number : "))
    if number == guess:
        print("Bravo! guessed it right ")
    elif number < guess:
        print("must be lower")
    elif number > guess:
        print("must be higher")
    i+= 1













