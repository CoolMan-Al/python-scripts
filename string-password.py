#!/usr/bin/python3
from random import randint, choice, shuffle
from string import digits, ascii_letters, punctuation

if __name__ == '__main__':
    # All char types are stored in one array
    # The output is a char array
    allChars = [ascii_letters, digits, punctuation]
    password = []

    # Iterate through each char type
    for charType in range(len(allChars)):
        # Will add random characters to output array
        for charCount in range(randint(5,15)):
            nextChar = choice(allChars[charType])
            password.append(nextChar)

    # Char array is shuffled
    shuffle(password)
    # All chars in char array is then sent into a string an outputted
    print(''.join(password))
