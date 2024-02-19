#  Write a program that reads a restaurant menu file (text or CSV) and stores items, prices, and 
# categories in a dictionary. Allow users to browse by category or search for specific items.# Define a dictionary to store Pakistani food categories and items
# Define a dictionary to store Pakistani food categories and items
pakistani_food = {
    "Appetizers": {
        "samosa": 20,
        "pakora": 25,
        "chana Chaat": 30,
        "dahi Baray": 40,
        "aloo Tikki": 35,
        "papri Chaat": 45,
        "fruit Chaat": 50,
        "haleem": 60,
    },
    "Main Course": {
        "biryani": 300,
        "karhai": 250,
        "nihari": 280,
        "pulao": 200,
        "korma": 220,
        "chicken Handi": 180,
        "daal Chawal": 150,
        "sajji": 400,
    },
    "Breads": {
        "naan": 25,
        "roti": 10,
        "paratha": 40,
        "chapati": 15,
        "sheermal": 50,
        "taftan": 60,
    },
    "BBQ": {
        "seekh kabab": 60,
        "boti kabab": 70,
        "reshmi kabab": 80,
        "tikka": 90,
        "chicken chargha": 120,
        "behari boti": 100,
        "malai boti": 110,
    },
    "Vegetarian": {
        "palak paneer": 200,
        "aloo gobi": 180,
        "baingan bharta": 150,
        "mix vegetable curry": 170,
        "paneer tikka": 220,
        "chana masala": 160,
        "daal tadka": 130,
    },
    "Desserts": {
        "gulab jamun": 30,
        "ras malai": 40,
        "kheer": 50,
        "jalebi": 20,
        "firni": 35,
        "zarda": 45,
        "sohan Halwa": 60,
    },
    "Drinks": {
        "lassi": 40,
        "soda": 20,
        "juice": 30,
        "shakes": 50,
        "tea": 10,
        "coffee": 25,
        "falooda": 70,
    },
}


print("Pakistani Food Menu:")
for category, items in pakistani_food.items():
    print(f"\n{category}:")
    for item, price in items.items():
        print(f"{item}: Rs. {price}")

while True:
    search_item = input("\nEnter the food item you want to search for (or type 'exit' to quit): ")

    if search_item.lower() == 'exit':
        print("Exiting...")
        break

    found = False
    for category, items in pakistani_food.items():
        if search_item in items:
            found = True
            print(f"{search_item} found in {category}: Rs. {items[search_item]}")
            break

    if not found:
        print(f"{search_item} not found in any category.")
