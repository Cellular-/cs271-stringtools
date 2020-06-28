import re, glob, os

alphabet = 'abcdefghijklmnopqrstuvwxyz'
frequencies = {}

def setup():
    for letter in alphabet:
        frequencies[letter] = 0

    return glob.glob("./*.txt")

def stats():
    filenames = setup()

    with open("output/concatenation.txt", "w") as concat_file:
        for filename in filenames:
            with open(filename, "r") as text_file:
                for line in text_file:
                    concat_file.write(line)
                    for word in split_line(line):
                        fc = first_char(remove_spec_chars(word))
                        if fc in alphabet:
                            frequencies[fc] += 1

            concat_file.write("\n")

            write_frequencies(filename)

def print_frequencies():
    for k, v in frequencies.items():
        print(k, v, "\n")

def write_frequencies(filename):
    filename = filename.replace(".txt", "")
    with open(f"output/{filename}_stats.txt", "w") as file:
        for k, v in frequencies.items():
            file.write(f"{k} - {v}\n")

def split_line(line):
    return line.split(" ")

def remove_spec_chars(string):
    return re.sub('[^A-Za-z0-9]+', '', string)

def first_char(string):
    return string[:1].lower()

stats()