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
        self.custom = False
        self.key = find_key(file)
        self.result = self.search(self.key)
        self.header = self.prompt()
        self.folder = self.make_folder_name()

    def search(self, key):
        url = "https://www.ncbi.nlm.nih.gov/nuccore/" + key
        print()
        print('Searching for {}...'.format(key))
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        tag = soup.find_all("h1")
        if (tag[1] is not None):
            print('Search results: {}'.format(tag[1].text.strip()))
            return tag[1].text.strip()
        """if (tag):
            tag = tag.find('a')
            result = tag.contents[0]
            result = result[:result.find(',')]
            print()
            print('Search results: {}'.format(result))
            return result"""
        return 'No result found'

    def make_header(self, line, product):
        if self.custom:
            temp = self.header.split()
            header = '>{}_{} {}'.format(temp[0], product, temp[1])
        else:
            header = '>{}_{} {}'.format(self.header, product, self.make_folder_name())
        # header += ' ' + self.key + ":" + location(line)
        # header += ' ' + self.key + '\n'
        header += ' {}:{} {} \n'.format(self.key, location(line), self.key)
        return header

    def make_folder_name(self):
        if self.custom:
            result = self.header.split()
            return result[1]
        else:
            result = self.result.split()
            return '{}_{}'.format(name(result), strain(result))

    def make_file_name(self, product):
        x = 'n_'
        if self.header.find('_NA') == -1:
            x = 'e_'
        file = product + x + self.folder
        return file

    def prompt(self):
        result = self.result.split()
        header = '{}_{}_'.format(initial(result), strain(result))
        temp_header = header + 'xx_xx ' + self.make_folder_name()
        print('Suggested header: {}'.format(temp_header))
        if ask('Use suggested header?'):
            while True:
                host = input('Input host:')
                print('Header: {}{}_x {}'.format(header, host, self.make_folder_name()))
                if ask('Are you sure you want this header?'):
                    return header + host
        while True:
            header = input('Input header:')
            print('Header: {}'.format(header))
            if ask('Are you sure you want this header?'):
                self.custom = True
                return header


def find_key(file):
    line = file.readline()
    line = line[5:]
    if line[0:2] == 'NZ':
        key = 'NZ_'
    else:
        key = 'NC_'
    line = line[3:]
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
    index = result.index("strain") if "strain" in result else -1
    if index != -1:
        return result[index + 1].upper()
    if "-" in result:
        return result[2].replace('-','.')
    else:
        return result[2].strip() + result[3].strip()




def location(line):
    regex = '(?<=location=).*(?=])'
    cregex = '(?<=\().*(?=\))'
    re.compile(regex)
    m = re.search(regex, line)
    location = m.group(0)
    location = location.replace("..", "-")
    if location.startswith('complement'):
        location = re.search(cregex, location).group(0)
        return 'c' + location
    '''in case the stuff after the location gets attached'''
    if location.find("]") != -1:
        location = location[:location.find("]")]
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
