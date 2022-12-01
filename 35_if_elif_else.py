# show ticket pricing
age = int(input("Enter your age here : "))

if 0<age<=3:
    print("Your ticket is free")
elif 4<=age<=10:
    print("Your ticket fare will be 150 rs")
elif 11<=age<=60:
    print("Your ticket fare will be 200 rs")
else:
    print("Your ticke fare will be free of cost ")