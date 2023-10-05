file = open("input.txt", "r")

content = file.read()

file.close()

words = content.split()

word_count = len(words)

print(f"Number of words in the file: {word_count}")
