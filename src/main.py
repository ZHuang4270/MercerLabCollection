import folderparser as p
import tkinter as tk
from tkinter import filedialog

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


def main():
    print('Choose a folder to read from:')
    read = choose_file()
    print('Choose a folder to write to:')
    write = choose_file()
    products = input('Type in what products you want to search for separate by a space\n')
    products = products.split()
    # read ='C:/Users/lasia/Documents/workspace/MercerLab/MercerLabCollection/resources'
    # write = 'C:/Users/lasia/Desktop/Output'
    # products = '5'
    parser = p.FolderParser(read, write, products)
    parser.parse()


if __name__ == "__main__":
    main()
