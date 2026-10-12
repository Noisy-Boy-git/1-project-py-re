import random
ansower=int(input("guess a number between 1 and 10:"))
computer=random.randint(1,10)
while ansower !=computer:
    if ansower>=computer:
        print("too high!")
        ansower=int(input("guess again:"))
    else:
        print("too low!")
        ansower=int(input("guess again:"))
print("congratulation!  you guess the number!")