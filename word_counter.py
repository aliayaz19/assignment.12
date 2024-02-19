# Write a program that reads a sentence and counts the number of times each word appears. Use 
# a dictionary to store the word counts.
sentence = input("Enter a sentence: ")
words = sentence.split()
word_counts = {}
for word in words:
    word = word.lower()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
