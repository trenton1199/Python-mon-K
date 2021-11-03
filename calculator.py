question = input("do you want to add, minus, divide, multiply")
numberone = int(input("enter a number you want to " + question))
numbertwo = int(input("enter another number you want to " + question))
one = "minus"
two = "add"
three = "multiply"
four = "divide"
if question == one:
    print(numberone - numbertwo)
elif question == three:
    print(numberone * numbertwo)
elif question == four:
    print(numberone / numbertwo)

else:
    print(numberone + numbertwo)

earningsgoal = 1
earningsmonths = 2
