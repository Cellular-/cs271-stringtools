import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'
frequencies = {}

def setup():
    for letter in alphabet:
        frequencies[letter] = 0

def stats():
    setup()
    with open("test.txt", "r") as text_file:
        for line in text_file:
            for word in split_line(line):
                fc = first_char(remove_spec_chars(word))
                if fc in alphabet:
                    frequencies[fc] += 1

def print_frequencies():
    for k, v in frequencies.items():
        print(k, v, "\n")

def split_line(line):
    return line.split(" ")

def remove_spec_chars(string):
    return re.sub('[^A-Za-z0-9]+', '', string)

def first_char(string):
    return string[:1].lower()

stats()