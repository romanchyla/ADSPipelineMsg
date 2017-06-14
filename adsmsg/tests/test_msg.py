import sys
import os

import unittest
import adsmsg
from adsmsg import BibRecord
from adsmsg.msg import Msg

class TestMsg(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.proj_home = os.path.join(os.path.dirname(__file__), '../..')


    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_generic_methods(self):
        # keywords initialization
        b = BibRecord(bibcode='bibcode')
        self.assertEqual(b.bibcode, 'bibcode')
        self.assertEqual(b.data.bibcode, 'bibcode')
        
        b.bibcode = 'foobar'
        self.assertEqual(b.bibcode, 'foobar')
        self.assertEqual(b.data.bibcode, 'foobar')




if __name__ == '__main__':
    unittest.main()
