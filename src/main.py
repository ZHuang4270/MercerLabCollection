import folderparser as p
import tkinter as tk
from tkinter import filedialog

read = None
write = None
products = None

def exit():
    print('***Program finished***')
    quit()


def choose_file():
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askdirectory()
    if file:
        print(file)
    else:
        print('No folder selected')
        exit()
    return file

def ask():
    while (True):
        string = input()
        if string.upper() == 'Y':
            return True
        if string.upper() == 'N':
            return False
        else:
            print('Sorry, I didn\'t understand what you inputted')

def prompt():
    global read
    global write
    global products

    file = open('Mercer_recent', 'r+')
    read = file.readline().strip()
    write = file.readline().strip()
    products = file.readline()
    if read:
        print('\nWant to use recent read folder? [y/n]')
        print('Read Folder: ' + read)
        if not ask():
            print('Choose a folder to read from:')
            read = choose_file()

        print('\nWant to use recent write folder? [y/n]')
        print('Write Folder: ' + write)
        if not ask():
            print('Choose a folder to write to:')
            write = choose_file()

        print('\nWant to use recent products? [y/n]')
        print('Products: ' + products)
        products = products.split()
        if not ask():
            products = input('Type in the products you want to search for separate by a space\n')
            products = products.split()

def record_recent():
    file = open('Mercer_recent', 'w')
    file.write(read + '\n' + write + '\n' + " ".join(products))


def main():
    prompt()
    record_recent()
    parser = p.FolderParser(read, write, products)
    parser.parse()
    exit()

if __name__ == "__main__":
    main()

# TODO:
# Print search results
# Print suggested header
# Prompt user for the host
    #Figure out the hosts???
# Threading???