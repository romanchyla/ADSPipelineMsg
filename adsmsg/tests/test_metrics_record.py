
import unittest
from adsmsg.metrics_record import MetricsRecord

class TestMsg(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test(self):
        metrics_data = {'bibcode': '2003ASPC..295..361M', 'refereed': False, 'downloads': [0,0],
                        'reads': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]}
        m = MetricsRecord(**metrics_data)
        self.assertEqual(m.bibcode, metrics_data['bibcode'])
        self.assertEqual(m.refereed, metrics_data['refereed'])
        self.assertEqual(m.downloads, metrics_data['downloads'])
        self.assertEqual(m.reads, metrics_data['reads'])

if __name__ == '__main__':
    unittest.main()
