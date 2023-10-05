def filter_text(text, forbidden_word):
    replacement = '*' * len(forbidden_word)
    modified_text = text.replace(forbidden_word, replacement)
    replacements_count = text.count(forbidden_word)

    return modified_text, replacements_count


text = ("Alice was beginning to get very tired of sitting by her sister on the bank, "
        "and of having nothing to do: once or twice she had peeped into the book her sister was reading, "
        "but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversations?")

word_to_replace = 'book'

modified_text, replacements_count = filter_text(text, word_to_replace)

output_filename = "output.txt"

with open(output_filename, 'w') as file:
    file.write(modified_text)

print(f"Statistics: {replacements_count} replacements of the word '{word_to_replace}' were made.")
