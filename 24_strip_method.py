name= "         Harsh       it             "
dots = "......."
# lstrip() method
print(name + dots)
# to remove left space 
print(name.lstrip() + dots)
print(name.rstrip() + dots)

print(name.strip()+ dots)

# if name =    harsh     it     then it will not erase this space
print(name.replace(" ", "" )+dots)
# replace space ( " ") with no space ""




