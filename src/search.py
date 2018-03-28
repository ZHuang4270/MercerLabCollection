class Search:
    """
    Searches the RNA and creates names
    Encapsulates search results

    Attributes:
        result :
        header :
        folder :
        file :
    """

    def __init__(self, file):
        self.result = self.search(file)
        self.header = self.make_header()
        self.folder = self.make_folder_name()
        self.file = self.make_folder_name()

    def search(self, file):
        return "as"

    def make_header(self):
        return "asd"

    def make_header(self,line):
        

    def make_folder_name(self):
        return "foldername"

    def make_file_name(self,product):
        # x = 'n_'
        # if folder.find('_NA_') != -1:
        #     x = 'e_'
        # filename = writefile + 'S' + x + folder
        self.file = 'filename' + product
        return self.file
