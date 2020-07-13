
# THis is simple calculation program by Aryan
# Name : Aryan
'''
Author : Aryan
Date : 09 July 2020
Email :

'''
first = input("Enter Your Name: ")
second = float(input("Enter your First Number: "))
third = float(input("Enter your second number: "))


# Addition
result = (second + third)
print('hello %s, %.2f + %.2f = %.2f '%(first,second,third,result))

# Sub
result  = second - third 
print('%.2f - %.2f = %.2f '%(second,third,result))

#mul
result  = second * third 
print('%.2f * %.2f = %.2f '%(second,third,result))
#div
result  = second / third 
print('%.2f / %.2f = %.2f '%(second,third,result))

#modulus
result  = second
print('%.2f remainder %.2f = %.2f '%(second,third,result))

# power
result = second ** third
print('%.2f ** %.2f = %.2f '%(second,third,result))




'''
------
Name    Class   History    Geo   Civics
Aryan   8 Grade    99       98      100
Nishad  8 Grade    70       65       88
ashaz   8 Grade    99       97      100
-----

Maths Formula
(a+b)^3 = a^3+b^3+3ab(a-b)

---
Taking an Input from the user...

Formula is (a+b)^3 = a^3+b^3+3ab(a-b)

Explaination of Formula : 
...
....
...

Show me output of the Formula Result
----------

'''
second = float(input("Enter your First Number: "))
third = float(input("Enter your second number: "))
result = (second + third)**3
print(result)
worst = input('aryan')
best = input('ashaz')
lucky = input('nishad')
print('Name   grade geo his')
print('aryan',worst)
print('ashaz',best)
print('nishad',lucky)