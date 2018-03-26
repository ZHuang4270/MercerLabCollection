import os
import glob

"""
@author Lasia Lo
"""


class FolderParser:
    """Parses through a folder

       Attributes:
            folder : Name of folder to parse
    """
    def __init__(self,foldername):
        self.folder = glob.glob(foldername)

    def parse(self):

        print(os.getcwd())
        # for f in myfolder
        #     file = open(f, 'r')


print("asdsadsad")