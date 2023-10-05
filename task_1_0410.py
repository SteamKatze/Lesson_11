
def create_text_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)


text = "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversations?"
create_text_file("original.txt", text)


with open('original.txt', 'r') as file:

    words = file.read().split()

filtered_words = [word.strip('.,?!;:') for word in words if len(word) >= 7]

with open('filtered.txt', 'w') as output:
    for word in filtered_words:
        output.write(word + '\n')