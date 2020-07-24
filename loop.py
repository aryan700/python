
'''
loop is repitative execution using counter


for loop
while

aryanbiswal

for <<variable>> in iterable_item:
    statements to be executed


# while loop syntax
# 
while(condition):
    Statemetns to be executed

'''

# For loop example


for n in range(2,100):
    if n%2 == 0 :
        print(" %d is not prime" % n)
    else:
        print("%d is prime number " % n)
                



# Take an input from the user
name = input("first word")


# Revert the given string
r_name = name[::-1]

# Assign the reversed string to for loop
for n in r_name:
    print(n)


