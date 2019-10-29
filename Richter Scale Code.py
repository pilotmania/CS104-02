#Python Richter Scale Calculation
#Your first and last name: Vincent Fossetta
#Your ID: s1288702


richter = input("Enter the Richter scale value: ")
n = False

while n == False:
    if float(richter) < 0:
        print("Value must be greater than 0.")

    elif float(richter) >= 8.0:
        print("Most structures fall")
        n = True

    elif float(richter) >= 7.0:
        print("Many buildings destroyed")
        n = True

    elif float(richter) >= 6.0:
        print("Many builds considerably damaged, some collapse")
        n = True

    elif float(richter) >= 4.5:
        print("Damage to poorly constructed buildings")
        n = True

    else:
        print("No destruction of buildings")
        n = True


# test your program several times with the following values:
#   8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6
