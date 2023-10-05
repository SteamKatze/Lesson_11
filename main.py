file = open("original.txt", "r")

content = file.read()

file.close()

words = content.split()

filtered_words = [word for word in words if len(word) >= 7]

output_file = open("filtered.txt", "w")

for word in filtered_words:

    output_file.write(word + '\n')

output_file.close()
