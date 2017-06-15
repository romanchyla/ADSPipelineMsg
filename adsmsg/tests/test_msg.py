import sys
import os

import unittest
import adsmsg
from adsmsg import BibRecord
from adsmsg.msg import Msg

class TestMsg(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_generic_methods(self):
        # keywords initialization
        b = BibRecord(bibcode='bibcode')
        self.assertEqual(b.bibcode, 'bibcode')
        self.assertEqual(b.data.bibcode, 'bibcode')
        
        # acces/set attributes directly
        b.bibcode = 'foobar'
        self.assertEqual(b.bibcode, 'foobar')
        self.assertEqual(b.data.bibcode, 'foobar')
        




if __name__ == '__main__':
    unittest.main()
