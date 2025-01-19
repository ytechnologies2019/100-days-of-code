items = { "Hammer" : 500 , "Bicycle" : 1000 , "Car" : 10000 }
item_list = list(items)
print (f"Now we will sell the {item_list[0]} for  ${items["Hammer"]}")

items = { "Hammer" : 500 , "Bicycle" : 1000 , "Car" : 10000 }
item_list = list(items)

buy_item = input(f"which item do you want to buy? : ")
print (f"Now we will sell the {item_list[0]} for  ${items["Hammer"]}")

remaining = False
while not remaining == True:
    user_input = input("Enter Your Name: ")
    user_pay = input("How many can you give? $")
    remaining_user = input("Any remaining users 'yes' or 'no' ")

    if remaining_user == "no":
        remaining = True
        pay = int(user_pay)
        if pay > items["Hammer"]:
            print (f"Winner is ${user_input}")
            break
    else:
        continue
