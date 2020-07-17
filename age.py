age = int(input("age:"))
agee = int(input("agee:"))

if age > agee:
    
    print(" %d year old age person is older"%(age))
    if age < 18:
        print("Hey, you are not an adult")
        if age < 10:
            print("Hey, You are a kid")
        else:
            print("Hey, You are growing...")
    else:
        print("Hey, You are now matured ")
elif age == agee:
    print("both %d year old  person and the other %d year old person are in same age"%(age,agee))
else:
    print("%d year old agee person is older"%(agee))  
