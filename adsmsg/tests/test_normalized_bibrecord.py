import sys
import os

import unittest
from adsmsg import NormalizedBibRecord
from adsmsg.tests import stubdata

class TestDenormalizedRecord(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.proj_home = os.path.join(os.path.dirname(__file__), '../..')


    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_is_valid(self):
        denormalized_record = NormalizedBibRecord()
        self.assertTrue(denormalized_record.is_valid())

    def test_serialization(self):
        abstract = "This is a dummy abstract."
        author = "Foe, J."
        author_count = 1

        denormalized_record = NormalizedBibRecord()
        denormalized_record.data.abstract = abstract
        denormalized_record.data.author.append(author)
        denormalized_record.data.author_count = author_count
        data = denormalized_record.serialize()
        self.assertEqual(data, '\n\x19{0}:\x07{1}@\x01'.format(abstract, author))
        data_str = str(denormalized_record)
        self.assertEqual(data_str, 'abstract: "{0}"\nauthor: "{1}"\nauthor_count: {2}\n'.format(abstract, author, author_count))
        self.assertNotEqual(data, data_str)

        recovered_bibrecord = NormalizedBibRecord.deserializer(data)
        self.assertTrue(recovered_bibrecord.is_valid())
        self.assertEqual(denormalized_record.data.abstract, abstract)
        self.assertEqual(denormalized_record.data.author[0], author)
        self.assertEqual(denormalized_record.data.author_count, author_count)
        
        
    def test_full_record(self):
        r = NormalizedBibRecord(**stubdata.solr_record)
        print r

if __name__ == '__main__':
    unittest.main()
