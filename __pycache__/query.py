"""Command line interface to query the stock.
To iterate the source data you can use the following structure:
for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

def bye(name:str) -> None:
    print(f'Thank you for your visit,{name}')

def option1(name: str, warehouse1: list, warehouse2: list)->None:
    print('')
    print('*************************')
    print('Items in warehouse 1:')
    print('*************************')
    print('')
    for item in warehouse1:
        print('- ' + item)
    print('')
    print('*************************')
    print('Items in warehouse 2:')
    print('*************************')
    print('')
    for item in warehouse2:
        print('- ' + item)
    print('')
    bye(name)

print('                                 ***Welcome to the our warehouse ***\n\n'            )






user_name = input("Please enter your name: ")
bye(user_name)

print(f"Hello, {user_name}")
print('Choose one of the follwoing options:')
print('To list the items press 1:')
print('To search an item and place an order press 2:')
print('To quit press 3:')

while True:
    user_input = input("Enter your opiton please: ")


    if user_input == "1":
        option1('User_name', warehouse1, warehouse2)
        break
   

 
    elif user_input == "2":
        item_name = input('What is the name of the item?')
        amount_warehouse1 = warehouse1.count(item_name)
        amount_warehouse2 = warehouse2.count(item_name)
       
        if amount_warehouse1 > 0 and amount_warehouse2 == 0:
            print(f"Amount available: {amount_warehouse1 + amount_warehouse2}")
            print('Location: Warehouse 1')

            yes_no = input("Would you like to order this item?(y/n) ")
            if yes_no.lower() == 'y':
                print(f"")
            else:
                print(f"Thank you for your visit, {user_name}")
                break
        
        if amount_warehouse1 == 0 and amount_warehouse2 > 0:
            print(f"Amount available: {amount_warehouse1 + amount_warehouse2}")
            print('Location: Warehouse 2')

            yes_no = input("Would you like to order this item?(y/n) ")
            if yes_no.lower() == 'y':
                print(f"")
            else:
                print(f"Thank you for your visit, {user_name}")
                break
        
        if amount_warehouse1 > 0 and amount_warehouse2 > 0:
            warehouse_dict = {amount_warehouse1: "warehouse1", amount_warehouse2: "warehouse2"}
            sum_items = amount_warehouse1 + amount_warehouse2
            maximum = max(amount_warehouse1, amount_warehouse2)
            print(f"Amount available: {sum_items}")
            print('Location: Both Warehouses')
            print(f"Maximum availability {maximum} in {warehouse_dict[maximum]}")


            yes_no = input("Would you like to order this item?(y/n) ")
            if yes_no.lower() == 'y':
                order_amount = int(input('How many would you like? '))
                if order_amount > sum_items:
                    print('***************************')
                    print(f'There are not this many available. The maximum amount that can be ordered is {sum_items}')
                    print('***************************')
                    order_max = input("Would you like to order the maximum available?(y/n) ")
                    if order_max.lower() == 'y':
                        print(f"{sum_items} {item_name} have been ordered.")
                        print('')
                        bye(user_name)
                        break
                    else:
                        print('')
                        bye(user_name)
                        break
                else:
                    print(f"{order_amount} {item_name} have been ordered.")
                    print('')
                    bye(user_name)
                    break

            else:
                bye(user_name)
                break
        else:
            print(f"Amount available: {amount_warehouse1 + amount_warehouse2}")
            print("Location: Not in stock")
            print('')
            bye(user_name)
   
    elif user_input == "3":
        bye(user_name)
        break
   

   

    else:
        print('')
        print('***********************')
        print(f'{user_input} is not a valid operation.')
        print('***********************')
        print('')
        bye(user_name)