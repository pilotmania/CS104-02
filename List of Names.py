names  = []
n1 = input("enter first name:")
n2 = input ("enter next name:")
n3 = input ("enter next name:")
n4 = input ("enter next name:")
n5 = input ("enter next name:")
n6 = input ("enter next name:")
n7 = input ("enter next name:")
n8 = input ("enter next name:")
n9 = input ("enter next name:")
n10 = input ("enter the last name:")
names.append(n1)
names.append(n2)
names.append(n3)
names.append(n4)
names.append(n5)
names.append(n6)
names.append(n7)
names.append(n8)
names.append(n9)
names.append(n10)

search = input("Enter a name to search for or 'End' to end the program: ")

while search in names:
    print("The name was found")

else:
    print ("The name was not found")
    input("Enter a name to search for or 'End' to end the program: ")
