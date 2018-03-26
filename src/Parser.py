import glob
import os
"""
@author Lasia Lo
"""


class FolderParser:
    """Parses through a folder

       Attributes:
            folder : Name of folder to parse
    """
    def __init__(self,foldername):
        self.folderpath = glob.glob(foldername + '/*.FNA')

    def store_name(self):
        
    def parse(self):
        print(self.folderpath)
        for f in self.folderpath:
            filename = os.path.basename(f)
            print(os.path.splitext(filename)[0])

            file =

