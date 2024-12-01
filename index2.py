num = int(input("enter your amount of money"))

numberof500=num//500
numberof200 = (num%500)//200
numberof100 = ((num%500)%200)//100
print("you need ",numberof500,"500 rupee is needed")
print("you need ",numberof200,"of 200 is needed")
print("you need ",numberof100,"of 100 is needed")
