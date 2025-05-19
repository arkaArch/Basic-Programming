import os, math
from pathlib import Path

def calculate_size_no_depth(path):
    # os.listdir('/home/arka/arch-dots') gives the folders name as a list
    # os.path.join('/home/arka/arch-dots', '.gitignore') outputs -> '/home/arka/arch-dots/.gitignore'
    # So to get the total size of 'arch-dots' folder in bytes
    total_size = 0
    for filename in os.listdir(path):
        total_size += os.path.getsize(os.path.join(path, filename))
    return total_size

def calculate_size(path):
    total_size = 0
    for folder_path, folders, files in os.walk(path):
        for filename in files:
            total_size += os.path.getsize(os.path.join(folder_path, filename))
    return total_size

def print_in_size(size):
    if size > 1000 * 1000 * 1000:
        print(str(math.floor(size / (1000 * 1000 * 1000))) + 'G')
    if size > 1000 * 1000:
        print(str(math.floor(size / (1000 * 1000))) + 'M')
    elif size > 1000:
        print(str(math.floor(size / 1000)) + 'K')
    else:
        print(str(size) + 'B')

path = input("Enter absolute path name: ")

if Path(path).exists():
    print_in_size(calculate_size(path))
else:
    print("Path doesn't exist")
