import glob
import os


class FolderParser:
    # """Parses through a folder
    #
    #    Attributes:
    #         read : Name of folderpath to parse
    #         write : Name of folderpath to write to
    #         products: List of products to identiy
    # """

    def __init__(self, read, write, product):
        self.read = glob.glob(read + '/*.FNA')
        self.write = write
        self.products = product

    # def is_product(self):

    def parse(self):
        for f in self.read:
            self.create_folder(f)

            file = open(f, 'r')

            # for line in file:
            #     line = line.split()
            #     if line.__contains__()
            #     if self.is_header(line):
            #         print(line)
            #         print(line.split())
            #         print('------------')

    def create_folder(self, filename):
        filename = os.path.basename(filename)
        filename = os.path.splitext(filename)[0]
        directory = self.write + '/' + filename
        if not os.path.exists(directory):
            os.makedirs(directory)
            # for s in self.products:

    def is_header(self, line):
        return line[0] == '>'

def why():
    print("why")