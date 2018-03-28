import glob
import os
import search as s

class FolderParser:
    """Parses through a folder

       Attributes:
            read : Name of folderpath to parse
            write : Name of folderpath to write to
            products: List of products to identiy
    """

    def __init__(self, read, write, products):
        self.read = glob.glob(read + '/*.FNA')
        self.write = write
        self.products = products

    def parse(self):
        for f in self.read:
            file = open(f, 'r')
            # suggest a header and use that to make a foldername
            search = s.Search(file)
            folder = self.create_folder(header)
            writefile = 'NULL'
            for line in file:
                if line[0] == '>':
                    writefile = self.product(line)
                if writefile != 'NULL':
                    self.write_to(folder, writefile)

    def create_folder(self, header):
        foldername = make_folder_name(header)
        directory = self.write + '/' + foldername
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory

    def product(self, line):
        to_return = 'NULL'
        for p in self.products:
            key = 'product=' + p + 'S'
            if line.find(key) != -1:
                to_return = p
        return to_return

    def write_to(self, folder, writefile):
        x = 'n_'
        if folder.find('_NA_') != -1:
            x = 'e_'
        filename = writefile + 'S' + x + folder
        file = open(writefile, 'w')
