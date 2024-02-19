#  Create a program that stores names and phone numbers in a dictionary. Offer options to 
# add, search, and update contacts.
number = {}

while True:
    print("\nOptions:")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. Update a contact's phone number")
    print("4. Exit")
    
    choice = input("Input your Choice: ")
    
    if choice == "1":
        while True:
            name = input("Enter a name (or type 'done' to stop): ")
            if name.lower() == 'done':
                break
            try:
                num = int(input("Enter a phone number: "))
                number[name] = num
                print(f"Contact '{name}' added.")
            except ValueError:
                print("Please enter a valid phone number (digits only).")
    elif choice == '2':
        name = input("Enter the name to search for: ")
        if name in number:
            print(f"Phone number for {name}: {number[name]}")
        else:
            print(f"Contact '{name}' not found.")
    elif choice == '3':
        name = input("Enter the name to update: ")
        if name in number:
            new_num = int(input("Enter the new phone number: "))
            number[name] = new_num
            print(f"Phone number updated for {name}.")
        else:
            print(f"Contact '{name}' not found.")
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")
