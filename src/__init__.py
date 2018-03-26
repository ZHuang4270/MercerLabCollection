import Parser
import tkinter as tk
from tkinter import filedialog

def main():
    # root = tk.Tk()
    # root.withdraw()
    # file_path = filedialog.askdirectory()
    file_path = 'C:/Users/lasia/Documents/workspace/MercerLab/MercerLabCollection/resources'
    parser = Parser.FolderParser(file_path)
    parser.parse()


if __name__ == "__main__":
    main()