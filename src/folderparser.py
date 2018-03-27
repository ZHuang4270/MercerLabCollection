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
            folder = self.create_folder(f)

            file = open(f, 'r')
            writefile = 'NULL'
            for line in file:
                if line[0] == '>':
                    writefile = self.product(line)
                if writefile != 'NULL':
                    self.write_to(writefile)



    def create_folder(self, filename):
        filename = os.path.basename(filename)
        filename = os.path.splitext(filename)[0]
        directory = self.write + '/' + filename
        if not os.path.exists(directory):
            os.makedirs(directory)
            # for s in self.products:
                #make a file for each s
        return

    def product(self, line):
        to_return = 'NULL'
        for p in self.products:
            key = 'product=' + p + 'S'
            if line.find(key) != -1:
                to_return = p
        return to_return

    def write_to(self,writefile):
        pass
