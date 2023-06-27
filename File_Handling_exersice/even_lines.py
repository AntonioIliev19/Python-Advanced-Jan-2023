import os

symbols = ["-", ",", ".", "!", "?"]

file_name = "files/text.txt"
path_to_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_dir, file_name)

with open(file_name, "r") as file:
    text = file.readlines()

for row in range(0, len(text), 2):

    for symbol in symbols:
        text[row] = text[row].replace(symbol, "@")

    print(*text[row].split()[::-1], sep=" ")