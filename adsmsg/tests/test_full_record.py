import sys
import os

import unittest
from adsmsg import FullRecord
from adsmsg import Msg


class TestFullRecord(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.proj_home = os.path.join(os.path.dirname(__file__), '../..')


    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_is_valid(self):
        full_record = FullRecord()
        self.assertFalse(full_record.is_valid())
        full_record.data.bibcode = "2017IAUS..325..341B"
        full_record.data.JSON_fingerprint = "JSON"
        full_record.data.metadata.general.arxivcategories.append("Instrumentation and Methods for Astrophysics")
        full_record.data.text.body.content = "Article..."
        self.assertTrue(full_record.is_valid())

    def test_serialization(self):
        bibcode = "2017IAUS..325..341B"
        JSON_fingerprint = "JSON"
        arxiv_category = "Instrumentation and Methods for Astrophysics"
        content = "This is a dummy article."

        full_record = FullRecord()
        full_record.data.bibcode = bibcode
        full_record.data.JSON_fingerprint = JSON_fingerprint
        full_record.data.metadata.general.arxivcategories.append(arxiv_category)
        full_record.data.text.body.content = content
        data = FullRecord.serializer(full_record)
        self.assertEqual(data, '\n\x13{0}\x12\x04{1}\x1a0\n.\n,{2}"\x1c\n\x1a\n\x18{3}'.format(bibcode, JSON_fingerprint, arxiv_category, content))

        recovered_full_record = FullRecord.deserializer(data)
        self.assertTrue(recovered_full_record.is_valid())
        self.assertEqual(full_record.data.bibcode, bibcode)
        self.assertEqual(full_record.data.JSON_fingerprint, JSON_fingerprint)
        self.assertEqual(full_record.data.metadata.general.arxivcategories[0], arxiv_category)
        self.assertEqual(full_record.data.text.body.content, content)




if __name__ == '__main__':
    unittest.main()
