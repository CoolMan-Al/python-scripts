#!/usr/bin/env python3

from sys import argv
from string import digits
from random import choice


def gen_initials(names):
    initials = ''
    for j in range(len(names)):
        letter = names[j][0].lower()
        initials += f'{letter}.'
    return initials


def gen_uuid():
    uuid = ''.join([choice(digits) for k in range(4)])
    return uuid


if __name__ == '__main__':

    try:
        student_list = open(argv[1]).read().splitlines()

        for i in range(0, len(student_list)):
            student_line = (student_list[i]).split(",")

            id_surname = student_line[0].split(' ')
            first_names = student_line[1].split(' ')
            first_names.pop(0)

            student_email = gen_initials(first_names)
            student_email += id_surname[1].lower() + gen_uuid()
            student_email += '@poppleton.ac.uk'

            output = open('output.txt', 'a')
            output.write(f"{id_surname[0]} {student_email} \n")
        
        print("Data processed. Stored in 'output.txt' in same directory as script.")

    except IndexError:
        print('Error. Command-line argument is missing or unusable.')
