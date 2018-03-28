class Search:
    """
    Searches the RNA and creates names

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
        self.file = self.make_file_name()

    def search(self, file):
        return "as"

    def make_header(self):
        return "asd"

    def make_folder_name(self):
        return "sdad"

    def make_file_name(self):
        return "adadsd"
