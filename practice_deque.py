from collections import deque

def is_palindrome(word):
    word = word.casefold().strip().replace(' ', '')
    char_deque = deque(word)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

input_word = input("Введіть слово: ")

if is_palindrome(input_word):
    print(f"{input_word} - це паліндром.")
else:
    print(f"{input_word} - не паліндром.")