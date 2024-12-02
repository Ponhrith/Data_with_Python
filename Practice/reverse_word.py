word = input("Enter a word: ")

reverse_word = ""
size = len(word) - 1

# while size >= 0:
#     char = word[size]
#     reverse_word += char
#     size -= 1

for letter in word:
    reverse_word = letter + reverse_word
print("The reversed word is: ", reverse_word)