#replace method
string = "she is beautiful and she is a good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was"))
print(string.replace("is","was",1)) #then it will replace only 1st is

#find method 

print(string.find("is")) #first "is"
print(string.find("is",6))

#
is_pos_1 = string.find("is")
# is_pos_2 = string.find("is", is_pos_1) #it will onlyshow the above position 4 because we are starting from 4 itself
is_pos_2 = string.find("is", (is_pos_1+1))
print(is_pos_1)
print(is_pos_2)


