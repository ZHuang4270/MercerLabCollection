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
        self.header = self.make_header(None, None)
        self.folder = self.make_folder_name()
        self.file = self.make_folder_name()

    def search(self, key):
        url = "https://www.ncbi.nlm.nih.gov/gene/?term=" + key
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        tag = soup.find('div', 'sensor_content')
        tag = tag.find('a')
        result = tag.contents[0]
        result = result[:result.find(',')]
        return result

    def make_header(self, line, product):
        header = ''
        result = self.result.split()
        if line == None:
            print(self.result)

            print(name(result))
            header += initial(result) + '_'
            header += strain(result) + '_'
            header += prompt()
            return header
        header += '_' + product + 'S'
        header += ' ' + name(result) + '_' + strain(result)
        header += ' ' + self.key + location(line)
        header += ' ' + self.key
        return header

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


def name(result):
    return result[0] + '_' + result[1]


def initial(result):
    return result[0][0].upper() + result[1][0:2].lower()


def strain(result):
    index = result.index('str.') if 'str.' in result else -1
    if index != -1:
        return result[index + 1]
    return result[-1]


def location(line):
    regex = '(?<=location=).*(?=])'
    m = re.search(regex, line)
    if m:
        location = m.group(1)
    print(location)
    # if line.find('location') != -1:
    #     to_return = p
    return 'asd'


def prompt():
    return ''
