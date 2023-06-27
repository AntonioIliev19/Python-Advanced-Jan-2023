import os

file_name = "my_first_file.txt"
path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, file_name)

try:
    os.remove(file_name)
except FileNotFoundError:
    print("File already deleted!")
