import unittest

import folderparser as p

class FolderTest(unittest.TestCase):

    def test_read(self):
        """
        Tests whether the parser correctly stores the read directory
        """
        read = 'C:/Users/lasia/Documents/workspace/MercerLab/MercerLabCollection/resources'
        write = ''
        products = ''
        parser = p.FolderParser(read, write, products)
        self.assertEqual(parser.read, glob.glob(read + '/*.FNA'))



if __name__ == '__main__':
    unittest.main()
