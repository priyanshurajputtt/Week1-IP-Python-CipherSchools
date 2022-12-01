name, char = input("Write the comma seperated name and char :\n" ).split(",")
print(f"length of the name is :{len(name)} and count of char {char} is {name.count(char)}") #case sensitive
'''Write the comma seperated name and char :
Anshaj Shukla, A
length of the name is :13 and count of char  A is 0
here it counts " A" as a character hence showing count 0 '''
print(f"length of the name is :{len(name)} and count of char {char.strip.lower()} is {name.strip().lower().count(char.strip.lower())}") #case sensitive

print(f"length of the name is {len(name)} and coount of char {char} is {name.strip().lower().count(char.lower())}")