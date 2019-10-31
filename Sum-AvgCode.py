#Sum/Average Program
#Your first and last name: Vincent Fossetta
#Your student ID: s1288702


numberList = []
input("Enter a number: ")

for x in range (0,20):
    a=int(input(""))
    numberList.append(int(a))
sm=sum(numberList)
avg=sm/x
print("The sum of the numbers you entered is: ",sm)
print("The average of the numbers you entered is: ",avg)
