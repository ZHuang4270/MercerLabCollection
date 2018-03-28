import requests
import re
from bs4 import BeautifulSoup

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
        self.key = find_key(file)
        self.result = self.search(self.key)
        self.header = self.make_header(None)
        self.folder = self.make_folder_name()
        self.file = self.make_folder_name()

    def search(self, key):
        url = "https://www.ncbi.nlm.nih.gov/gene/?term=" + key
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        string = soup.find('div', 'sensor_content')
        string = string.find('a')
        string = string.contents[0]
        string = string[:string.find(',')]
        return string

    def make_header(self, line):
        pass

    def make_folder_name(self):
        return "foldername"

    def make_file_name(self, product):
        # x = 'n_'
        # if folder.find('_NA_') != -1:
        #     x = 'e_'
        # filename = writefile + 'S' + x + folder
        self.file = 'filename' + product
        return self.file


def find_key(file):
    line = file.readline()
    line = line[8:]
    key = 'NC_'
    for s in line:
        if s == '_':
            print(s)
            break
        key += s
    return key
