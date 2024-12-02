word = input("Enter a word: ")

reverse_word = ""
size = len(word) - 1

while size >= 0:
    char = word[size]
    reverse_word += char
    size -= 1
print("The reverse word is: ", reverse_word)