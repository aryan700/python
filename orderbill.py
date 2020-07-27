


'''
First Take Customer name  and Table No


'''
customer_name = input("Customer Name : ")
customer_table = int(input("Table Number : "))

# Items
total_items = int(input("Total Items: "))

# list creation
item_name = []
item_quantity = []
item_price = []


for count in range(0, total_items):
    print(count)
    list_item_name = input("Item Name : ")
    list_item_quantity = int(input("Item Quantity: "))
    list_item_price = int(input("Item Price: "))

    item_name.append(list_item_name)
    item_quantity.append(list_item_quantity)
    item_price.append(list_item_price)



# Price
'''
print(item_name)
print(item_quantity)
print(item_price) 


print
print(sum(item_price))
'''

# Printing Bill
bill =('''
---------------------------------
ARYAN HOTEL  BILLING SOFTWARE
---------------------------------
Customer Name: {0}
Table : {1}
----------------------------------
No.     Item        Quantity         Price
---------------------------------
''').format(customer_name, customer_table)

print(bill)
for count in range(0,total_items):
    print(count, "\t" , item_name[count], "\t",item_quantity[count], "\t", item_price[count])
print("---------------------------------")
print("       Total", "\t", sum(item_quantity), "\t", sum(item_price)) 
print("---------------------------------")