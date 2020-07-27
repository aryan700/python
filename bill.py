print("                    WELCOME TO ARE HOTEL")

print("You can order from these")
print("masala-dosa")
print("idli")
print("vada")
print("tea")
print("              What would you like to order today")
x=20

dosaPrice = 40
idliPrice = 20
vadaPrice = 30
teaPrice = 10


item_1 = input("first item:")
quantity_1 = input("quantity:")
if item_1 == "no" or item_1 == "nothing":
    print("ok")    


item_2 = input("second item:")
quantity_2 = input("quantity:")
if item_2 == "nothing" or item_2 == "no":
    print("ok")

item_3 = input("third item:")
quantity_3 = input("quantity:")
if item_3 == "nothing" or item_3 == "no":
    print("ok")

item_4 = input("fourth item:")
quantity_4 = ("quantity:")
if item_4 == "no" or item_4 == "nothing":
    print("ok")


print("         THE BILL     ")
print("       items     quantity     price")

if (item_1.strip().lower() == "masala dosa" ) or (item_2.strip().lower() == "masala dosa" ) or (item_3.strip().lower() == 'masala dosa' ) or (item_4.strip().lower() == 'masala dosa' ):
    price_1 = int(dosaPrice) * int(quantity_1)
    print(          item_1,   quantity_1,   price_1    )
if    (item_1.strip().lower() == "idli") or (item_2.strip().lower()== "idli") or (item_3.strip().lower()== 'idli') or (item_4.strip().lower() == 'idli') :
    price_2 =  int(idliPrice) * int(quantity_2)
    print(      item_2,   quantity_2,   price_2    )
if    (item_1.strip().lower() == "vada") or (item_2.strip().lower() == "vada") or (item_3.strip().lower() == 'vada') or (item_4.strip().lower() == 'vada') :
    price_3 =  int(vadaPrice) * int(quantity_3)
    print(      item_3,   quantity_3,   price_3    )
    
if  (item_1.strip().lower() == "tea") or (item_2.strip().lower() == "tea") or (item_3.strip().lower() == 'tea') or (item_4.strip().lower() == 'tea') :
    price_4 = int(teaPrice) * int(quantity_4 
    print(     item_4,   quantity_4,   price_4    )

    







        
