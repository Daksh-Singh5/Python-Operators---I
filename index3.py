num1 = int(input("enter your first number"))
num2 = int(input("enter your second number"))
num3 = int(input("enter your third number"))
num4 = int(input("enter your forth number"))
addnum = num1+num2+num3+num4
per = (addnum/400)*100
rounded = round(per,2)
print(rounded, "%")