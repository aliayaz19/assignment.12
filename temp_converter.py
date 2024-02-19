# Build a program that converts temperatures between Celsius and Fahrenheit using a dictionary 
# to store conversion factors.
# Define a dictionary to store conversion factors
conversion_factors = {
    "c_to_f": lambda c: c * 9 / 5 + 32, 
    "f_to_c": lambda f: (f - 32) * 5 / 9   
}


while True:
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = conversion_factors["c_to_f"](celsius)
        print(f"The temperature in Fahrenheit is: {fahrenheit}")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = conversion_factors["f_to_c"](fahrenheit)
        print(f"The temperature in Celsius is: {celsius}")
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
