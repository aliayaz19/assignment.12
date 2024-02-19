#  Develop a program that allows users to add, remove, and check off items on a shopping list 
# stored in a dictionary
shopping_list = {}

shopping_list["Apples"] = False  
shopping_list["Bananas"] = False
shopping_list["Milk"] = False

if "Bananas" in shopping_list:
    del shopping_list["Bananas"]
    print("Bananas removed from the shopping list.")
else:
    print("Bananas are not in the shopping list.")

if "Milk" in shopping_list:
    shopping_list["Milk"] = True
    print("Milk checked off.")
else:
    print("Milk is not in the shopping list.")

if "Apples" not in shopping_list:
    shopping_list["Apples"] = False
    print("Apples have been added to the shopping list.")

print("Updated shopping list:", shopping_list)
