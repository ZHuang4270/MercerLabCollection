import Parser
import tkinter as tk
from tkinter import filedialog

def main():
    parser = Parser.FileParser()
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    parse = Parser.FolderParser(file_path)
    print(file_path)


if __name__ == "__main__":
    main()