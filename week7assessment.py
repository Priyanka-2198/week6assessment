from collections import Counter

file_name = "my1_notes.txt"

file = open(file_name , "r")
text = file.read()
file.close()

words = text.split()
lines = text.split("\n")

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(text))

print("Top words:", Counter(words).most_common(3))