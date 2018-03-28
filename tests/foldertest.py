import unittest
import glob
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

    def test_write(self):
        read = 'C:/Users/lasia/Documents/workspace/MercerLab/MercerLabCollection/resources'
        write = 'C:/Users/lasia/Desktop/TestOutput'
        products = ''

if __name__ == '__main__':
    unittest.main()
