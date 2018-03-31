import glob
import os
import search as s


class FolderParser:
    """Parses through a folder, writes results to destination

       Attributes:
            read : Name of folderpath to parse
            write : Name of folderpath to write to
            products: List of products to identiy
            search : Encapsulates search results
    """
    def __init__(self, read, write, products):
        self.read = glob.glob(read + '/*.FNA')
        self.write_path = write
        self.products = products
        self.search = None

    def parse(self):
        for f in self.read:
            file = open(f, 'r')
            self.search = s.Search(file)
            folder = self.create_folder()
            product = 'NULL'
            for line in file:
                if is_header(line):
                    product = self.find_product(line)
                if product != 'NULL':
                    self.search.make_file_name(product)
                    self.write(line, folder, product)
            print('File finished')

    def find_product(self, line):
        to_return = 'NULL'
        for p in self.products:
            key = 'product=' + p + 'S'
            if line.find(key) != -1:
                to_return = p
        return to_return

    def create_folder(self):
        folder_name = self.search.folder
        directory = self.write_path + '/' + folder_name
        if not os.path.exists(directory):
            os.makedirs(directory)
        directory += '/'
        self.clear(directory)
        return directory

    def clear(self, directory):
        for p in self.products:
            self.search.make_file_name(p)
            write_path = directory + self.search.make_file_name(p) + '.fasta'
            print('Writing to: ' + write_path)
            file = open(write_path, 'w')
            file.write('')

    def write(self, line, folder, product):
        write_path = folder + self.search.make_file_name(product) + '.fasta'
        file = open(write_path, 'a+')
        if is_header(line):
            line = self.search.make_header(line, product)
        file.write(line)

def is_header(line):
    return line[0] == '>'
