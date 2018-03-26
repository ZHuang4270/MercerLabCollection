
def main():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    parser = Parser.FolderParser(file_path)
    parser.parse()


if __name__ == "__main__":
    main()