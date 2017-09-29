
import unittest
from adsmsg import msg

from adsmsg.nonbibrecord import NonBibRecord

class TestMsg(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test(self):
        nonbib_data = {'bibcode': '2003ASPC..295..361M', 'refereed': False,
                       'downloads': [0,0], 'boost': 3.1,
                       'reads': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                       'data_links': {'a': ['b', 'c'], 'w': ['x', 'y', 'z']},
                       'total_link_counts': 20,
                       'esource': ['a', 's', 'd', 'f'],
                       'data': ['NED:15', 'CDS:5']}
        m = NonBibRecord(**nonbib_data)
        self.assertEqual(m.bibcode, nonbib_data['bibcode'])
        self.assertEqual(m.refereed, nonbib_data['refereed'])
        self.assertEqual(m.downloads, nonbib_data['downloads'])
        self.assertEqual(m.reads, nonbib_data['reads'])
        self.assertAlmostEqual(m.boost, nonbib_data['boost'], places=5)
        self.assertEqual(m.data_links['a'].value, nonbib_data['data_links']['a'])
        self.assertEqual(m.data_links['w'].value, nonbib_data['data_links']['w'])
        self.assertEqual(m.total_link_counts, nonbib_data['total_link_counts'])
        self.assertEqual(m.data.data, nonbib_data['data'])
        self.assertEqual(m.esource, nonbib_data['esource'])


if __name__ == '__main__':
    unittest.main()
