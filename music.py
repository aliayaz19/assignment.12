#  Develop a program that stores song titles, artists, and genres in a dictionary. Include functions to 
# sort by different criteria (title, artist, genre) and search for specific songs.while True:
while True:
    x = input("ENTER YOUR MOOD STATE: ")
    mood1 = "sad"
    mood2 = "romantic"
    mood3 = "chill"

    sad_songs = {
        "Chahun Main Ya Naa": "Aashiqui 2",
        "Raabta": "Agent Vinod",
        "Tum Hi Ho": "Aashiqui 2",
        "Phir Bhi Tumko Chaahunga": "Half Girlfriend",
        "Raabta (Title Track)": "Raabta",
        "KAISE HUA": "Kabir Singh",
        "Bekhayali mein": "Kabir Singh",
        "Agar Tum Saath Ho": "Tamasha",
        "Mujhe peene do": "By Darshan Raval",
        "Tera Ban Jaunga": "Kabir Singh"
    }

    romantic_songs = {
        "Maan Meri Jaan": "By King",
        "Chaand Sifarish": "Fanna",
        "Tera Mera Hai Pyar Amar": "Ishq Murshad",
        "Tere Hawale": "Laal Singh Chaddha",
        "Dill Diyan Gallan": "Tiger Zinda Hai",
        "Zaalima": "Raees",
        "Pehli Dafa": "Atif Aslam",
        "O Sathi": "Baaghi 2",
        "Dekhte Dekhte": "Batti Gul Meter Chalu",
        "O Re Piya": "Aaja Nachle"
    }

    chilling_songs = {
        "Har Funn Maula": "Koi Jaane Na",
        "King Shit": "Shubh",
        "Kusu Kusu": "Satyameva Jayate 2",
        "Afghan Jalebi": "Phantom",
        "Softly": "Karan Aujila",
        "Favicol Se": "Dabangg 2",
        "Param Sundri": "Mimi",
        "Kuley Kuley": "By Honey Singh",
        "Sunny Sunny": "Yariyan",
        "White Brown Black": "Karan Aujila"
    }

    if x == mood1:
        print(sad_songs)
    elif x == mood2:
        print(romantic_songs)
    elif x == mood3:
        print(chilling_songs)
    else:
        print("No Record Found!")

    user_input = input("Do You Want To Continue (YES/NO): ")
    if user_input.upper() != "YES":
        break