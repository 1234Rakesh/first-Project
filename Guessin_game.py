import random

jackport = random.randint(1,100)
guess = int(input("Guess a number: "))
counter = 1

while guess != jackport:
    if guess < jackport:
        print("Guess higher")
    else:
        print("Guess Lower")
        
    guess = int(input("Guess a number"))
    counter +=1
    
print("you are Courect!")
print("you took",counter,"attempts")