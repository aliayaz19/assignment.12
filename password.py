#  Design a simple program that generates random passwords from a set of characters 
# (lowercase, uppercase, numbers, symbols). The password length and character limitations can 
# be stored in a dictionary.
import random

rdm_characters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
    "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "!", "@", "#", "$",
    "%", "^", "&", "*", "/", "?"
]
rdm_dictionary={}
rdm_characters=rdm_dictionary
for _ in range(8):
    print(random.choice(rdm_characters), end="")
    
