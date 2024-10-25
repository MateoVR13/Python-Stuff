# Exercise 6: Shopping List

# - Write a program that allows the user to manage a shopping list. The program should:
#     - Allow the user to add items to the list.
#     - Remove items from the list.
#     - Print the list.
#     - Save the list to a file and load it from the file.

from pprint import pprint

print("\n------------ Welcome to Shopping List ------------")
print("Enter 1 to watch your shopping list.")
print("Enter 2 to add an item to the shopping list.")
print("Enter 3 to remove an item from the shopping list.")
print("Enter 4 to save shopping list into a file.")
print("Enter 5 to load a shopping list from a file.")
print("Enter 6 to repeat the option list.")
print("Enter 0 to exit the program.")

shopping_cart = []

while True:
        
    ent_1 = int(input("\nPlease enter your option: "))
    
    if ent_1 == 1:
        
        pprint(shopping_cart)
        
    elif ent_1 == 2:
       
       print("\n----------- Adding Items ----------")
       print("You can add as many items you want.")
       print("Type 'exit' to return to menu.\n")
       ent_2 = ""
       
       while ent_2 != "exit": 
            
            ent_2 = input("Enter the new item: ")
            shopping_cart.append(ent_2)
            print(f"{ent_2} was added to the list!\n")
            
            if ent_2 == "exit":
                
                shopping_cart.remove(ent_2)
                pprint(f"The new shopping list is: {shopping_cart}")
                print("Returning to menu... \n")
         
    elif ent_1 == 3:
        
        ent_3 = ""
        print("\n-------- Removing Items ---------")
        print("You can remove as many items you want.")
        print("Type 'exit' to return to menu.\n")
        
        while ent_3 != "exit": 
            
            ent_3 = input("Enter the item to be removed: ")
            if ent_3 == "exit":
                print("Returning to menu... \n")            
                break
            
            if ent_3 in shopping_cart:
                shopping_cart.remove(ent_3)
                print(f"{ent_3} was removed from the list!\n")
                pprint(f"New list is: {shopping_cart}")
            else:
                print(f"Item '{ent_3}' not found in the shopping cart.\n")
            
            
    elif ent_1 == 4:
        
        with open("shopping_list.txt", "w") as shp_list:
            
            shp_list.write(shopping_cart.split(","))
            print("The shopping list was saved as 'shopping_list.txt'")
            
            
    elif ent_1 == 5:
        
        with open("shopping_list.txt", "r") as file:
            
            file_content = file.read()
            pprint(f"The items in the {file.name} are: {file_content}")
            shopping_cart = file_content
    
    elif ent_1 == 0:
        print("Exiting program... \n") 
        break
    
    elif ent_1 == 6:
        
        print("Enter 1 to watch your shopping list.")
        print("Enter 2 to add an item to the shopping list.")
        print("Enter 3 to remove an item from the shopping list.")
        print("Enter 4 to save shopping list into a file.")
        print("Enter 5 to load a shopping list from a file.")
        print("Enter 6 to repeat the option list.")
        print("Enter 0 to exit the program.")