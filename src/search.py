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
            print(header)
            return header
        header = '>' + self.header
        header += '_' + product + 'S'
        header += ' ' + self.make_folder_name()
        header += ' ' + self.key + location(line)
        header += ' ' + self.key + '\n'
        return header

    def make_folder_name(self):
        result = self.result.split()
        return name(result) + '_' + strain(result)

    def make_file_name(self, product):
        x = 'n_'
        if self.header.find('_NA_') != -1:
            x = 'e_'
        file = product + 'S' + x + self.folder
        return file


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
    regex = '(?<=location=).*(?=] )'
    cregex = '(?<=\().*(?=\))'
    re.compile(regex)
    m = re.search(regex, line)
    location = m.group(0)
    if location.startswith('complement'):
        location = re.search(cregex, location).group(0)
        return 'c' + location
    return location


def prompt():
    return ''
