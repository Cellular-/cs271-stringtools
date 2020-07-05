import re, glob, os, editdistance, itertools

pref = input("Print output to screen or write output to files in `output` folder? ")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
frequencies = {}
filenames = [os.path.basename(filename) for filename in glob.glob("./*.txt") if os.path.basename(filename) != 'words.txt']
output_basename = "output/{filename}_stats.txt"
output_filenames = [output_basename.format(filename=filename.replace(".txt", "")) for filename in filenames]

log = None # function that will either hold ref to write or print functionality

def print_frequencies():
    print("Frequency results below:\n")
    for k, v in frequencies.items():
        print(k, v, "\n")

def write_frequencies():
    for filename in output_filenames:
        with open(filename, "w") as file:
            for k, v in frequencies.items():
                file.write(f"{k} - {v}\n")

    print("Writing frequencies to output folder!")

while pref not in ("print", "write"):
    print("Invalid parameter!")
    pref = input("Print output to screen or write output to files in `output` folder? (enter print or write) ")

if pref == "write":
    log = write_frequencies
elif pref == "print":
    log = print_frequencies

def setup():
    for filename in filenames:
        frequencies[filename] = {}
        for letter in alphabet:
            frequencies[filename][letter] = 0

def main():
    setup()
    
    with open("output/concatenation.txt", "w") as concat_file:
        for filename in filenames:
            if filename != 'words.txt':
                    with open(filename, "r") as text_file:
                            for line in text_file:
                                concat_file.write(line)
                                for word in split_line(line):
                                    fc = first_char(remove_spec_chars(word))
                                    if fc in alphabet and fc:
                                        frequencies[filename][fc] += 1

            concat_file.write("\n\n")

    with open("output/words_edit_distances.txt", "w") as file:
        for pair, edit_count in edit_distance_analysis().items():
            file.write(f"{pair}, {edit_count}\n")

    log()

def split_line(line):
    return line.split(" ")

def remove_spec_chars(string):
    return re.sub('[^A-Za-z0-9]+', '', string)

def first_char(string):
    return string[:1].lower()

def edit_distance(word1, word2):
    return editdistance.eval(word1, word2)

def test_edit_distance():
    word1 = "hello"
    word2 = "helo"

    return edit_distance(word1, word2) == 1

def edit_distance_analysis():
    words = []
    
    with open("words.txt", "r") as word_file:
        for word in word_file:
            words.append(remove_spec_chars(word))

    results = {}

    for pair in list(itertools.combinations(words, 2)):
        results[pair[0] + "-" + pair[1]] = edit_distance(pair[0], pair[1])

    return results

main()
edit_distance_analysis()