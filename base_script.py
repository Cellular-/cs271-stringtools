def stats():
    stats = {}
    with open("test.txt", "r") as text_file:
        for line in text_file:
            for word in split_line(line):
                print(word, "\n")

def split_line(line):
    return line.split(" ")

stats()