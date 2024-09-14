#!/usr/bin/env python3

from random import choice

DICTIONARY = [['Bored', 'Lively', 'Willing', 'Impressive', 'Cranky',
              'Calm', 'Impulsive', 'Unintelligible',
               'Abnormal', 'Unlucky', 'Friendly', 'Large', 'Boring',
               'Disillusioned', 'Freezing', 'Accurate', 'Enchanted',
               'Homely', 'Ludicrous', 'Practical', 'Roasted', 'Annoying',
               'Piquant', 'Capable', 'Illegal', 'Accessible', 'Efficacious',
               'Calm', 'Sour', 'Uptight'],
              ['Teal', 'Grey', 'Blue', 'Orange', 'Navy', 'Crimson', 'White',
              'Black', 'Pink', 'Magenta', 'Lavender', 'Yellow', 'Green',
               'Red', 'Cyan', 'Cobalt', 'Chestnut', 'Melon', 'Wine', 'Olive',
               'Vermilion', 'Violet', 'Gold', 'Beige', 'Mahogany',
               'Raspberry', 'Azure', 'Night', 'Moss', 'Brown'],
              ['Camel', 'Gorilla', 'Snake', 'Possum', 'Leopard', 'Fox',
              'Wolf', 'Lion', 'Rhino', 'Dog', 'Cat', 'Human', 'Crocodile',
               'Alligator', 'Owl', 'Cockatoo', 'Raven', 'Frog', 'Carp',
               'Chicken', 'Duck', 'Elephant', 'Tiger', 'Panther',
               'Giraffe', 'Ant', 'Dragon', 'Seagull', 'Bear', 'Snail']]

if __name__ == '__main__':
    print('Password Generator!')
    print('==================')

    while True:
        try:
            num_pass = int(input('How many passwords are needed? '))

            if num_pass < 1 or num_pass > 24:
                raise ValueError

            print('==================')

            i = 0
            while i < int(num_pass):
                password = ''

                for k in range(len(DICTIONARY)):
                    password += choice(DICTIONARY[k])
                print(f'{i + 1} --> {password}')

                i += 1
            print('==================')
            break

        except ValueError:
            print('Please enter a whole number between 1 and 24.')
