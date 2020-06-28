import re

def stats():
    stats = {}
    with open("test.txt", "r") as text_file:
        for line in text_file:
            for word in split_line(line):
                print(remove_spec_chars(word), "\n")

def split_line(line):
    return line.split(" ")

def remove_spec_chars(string):
    return re.sub('[^A-Za-z0-9]+', '', string)

stats()