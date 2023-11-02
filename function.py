# def my_function():
    
#     print(x)

# x=10
# my_function()
###NON-LOCAL SCOPE ###
# x=10
# def my_function():
#     global x 
#     x=20
# my_function()
# print(x)

import random
def guess_number():
    return random.randint(1,100)
target_number = guess_number()
attempts = 0
while True:
    n=int(input("guess the number"))
    attempts += 1
    if n==target_number :
        print("congratulation sucessful guess")
        print("guessed in",attempts,"attempts")
        break
    elif n<target_number :
        print("guess higher")
    else:
        print("guess lower")

