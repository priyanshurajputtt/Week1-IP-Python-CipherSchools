'''importing random number'''

import random
# n = random.random      #any random number

n = random.randint(1,10)

a = int(input("Enter any random lottery number\n"))

if n == a:
    print("you win tea from my side") 
else:
    print("better luck next time")

