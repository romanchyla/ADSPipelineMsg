
import unittest
from adsmsg.nonbibrecord import NonBibRecord

class TestMsg(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test(self):
        nonbib_data = {'bibcode': '2003ASPC..295..361M', 'refereed': False, 
                       'downloads': [0,0], 'boost': 3.1,
                       'reads': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]}
        m = NonBibRecord(**nonbib_data)
        self.assertEqual(m.bibcode, nonbib_data['bibcode'])
        self.assertEqual(m.refereed, nonbib_data['refereed'])
        self.assertEqual(m.downloads, nonbib_data['downloads'])
        self.assertEqual(m.reads, nonbib_data['reads'])
        self.assertEqual(m.boost, nonbib_data['boost'])


if __name__ == '__main__':
    unittest.main()
