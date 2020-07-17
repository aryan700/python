''' 
fruit = input("Enter Name: ")

if fruit.lower() ==  "apple" or fruit.lower() == "apples":
    print("its just an apple")
elif fruit == "Mango":
    print("its just  a mango")
elif fruit == "grapes":
    print("its just  grapes")
else: 
    print("don't know the name")


south 
North
east
west
northeast
northwest
southeast
southwest

Input can be :   "south or SOUTH or South or SoUtH
northwest or Northwest or NorthWest or NORTHWEST or NW or nw or northWest
'''
age = int(input("age:"))
agee = int(input("agee:"))
if age > agee:
    print(" %d year old age person is older"%(age))
elif age == agee:
    print("both %d year old  person and the other %d year old person are in same age"%(age,agee))
else:
    print("%d year old agee person is older"%(agee))  
