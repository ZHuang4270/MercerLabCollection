import requests
import re
from bs4 import BeautifulSoup


class Search:
    """
    Searches the RNA and creates names and
    encapsulates search results. Will prompt
    user to make changes

    Attributes:
        result : Result of search
        header : Header made by search
        folder : Folder path
        file : File path
    """

    def __init__(self, file):
        self.key = find_key(file)
        self.result = self.search(self.key)
        self.header = self.prompt()
        self.custom = False
        self.folder = self.make_folder_name()

    def search(self, key):
        url = "https://www.ncbi.nlm.nih.gov/gene/?term=" + key
        print()
        print('Searching for ' + key + ' ...')
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        tag = soup.find('div', 'sensor_content')
        tag = tag.find('a')
        result = tag.contents[0]
        result = result[:result.find(',')]
        print()
        print('Search results: ' + result)
        return result

    def make_header(self, line, product):
        if self.custom:
            temp = self.header.split()
            header = '>' + temp[0]
            header += '_' + product
            header += ' ' + temp[1]
        else:
            header = '>' + self.header
            header += '_' + product
            header += ' ' + self.make_folder_name()
        header += ' ' + self.key + ":" + location(line)
        header += ' ' + self.key + '\n'
        return header

    def make_folder_name(self):
        result = self.result.split()
        return name(result) + '_' + strain(result)

    def make_file_name(self, product):
        x = 'n_'
        if self.header.find('_NA_') != -1:
            x = 'e_'
        file = product + x + self.folder
        return file

    def prompt(self):
        result = self.result.split()
        header = initial(result) + '_' + strain(result) + '_'
        temp_header = header + 'xx_xx ' + self.make_folder_name()
        print('Suggested header: ' + temp_header)
        if ask('Use suggested header?'):
            while True:
                host = input('Input host:')
                print('Header: ' + header + host + '_xx ' + self.make_folder_name())
                if ask('Are you sure you want this header?'):
                    return header + host
        while True:
            header = input('Input header:')
            print('Header: ' + header)
            if ask('Are you sure you want this header?'):
                self.custom = True
                return header


def find_key(file):
    line = file.readline()
    line = line[8:]
    key = 'NC_'
    for s in line:
        if s == '_':
            break
        key += s
    return key


def name(result):
    return result[0] + '_' + result[1]


def initial(result):
    result = result[0][0].upper() + result[1][0:2].lower()
    return result.replace('-','.')


def strain(result):
    index = result.index('str.') if 'str.' in result else -1
    if index != -1:
        return result[index + 1].upper()
    return result[-1].upper().replace('-','.')


def location(line):
    regex = '(?<=location=).*(?=] )'
    cregex = '(?<=\().*(?=\))'
    re.compile(regex)
    m = re.search(regex, line)
    location = m.group(0)
    location = location.replace("..", "-")
    if location.startswith('complement'):
        location = re.search(cregex, location).group(0)
        return 'c' + location
    return location


def ask(question):
    if question:
        print(question + ' [y/n]')
    while (True):
        string = input()
        if string.upper() == 'Y':
            return True
        if string.upper() == 'N':
            return False
        else:
            print('Sorry, I didn\'t understand what you inputted')
