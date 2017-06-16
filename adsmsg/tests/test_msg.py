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
        
    
    def test_serializer(self):
        b = BibRecord(bibcode='bibcode')
        cls, data = b.dump()
        
        self.assertEqual('adsmsg.bibrecord.BibRecord', cls)
        
        b2 = Msg.loads(cls, data)
        self.assertEqual(b2.bibcode, b.bibcode)

    



if __name__ == '__main__':
    unittest.main()
