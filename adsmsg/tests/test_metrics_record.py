
import unittest
from adsmsg.metrics_record import MetricsRecord
from datetime import datetime
import time

class TestMsg(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_simple_data(self):
        """tests fields where output data that exactly matches input data, covers most fields"""
        metrics_data = {'bibcode': '1954PhRv...93..256R', 
                        'an_citations': 0.15625,
                        'an_refereed_citations': 0.2, 
                        'author_num': 4,
                        'citation_num': 11,
                        'citations': ["1954PhRv...93..257G", "1954PhRv...96..730K","1955PhRv...98...79M", "1956RScI...27..809A",
                                      "1958PhRv..112..543S", "1961RScI...32..621H","1963NucPh..45...41A", "1992NDS....67..327K",
                                      "2009NDS...110.2945S", "2013ADNDT..99...22K"],
                        'downloads': [0, 0],
                        'reads': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                        'refereed': False, 
                        'refereed_citation_num': 10,
                        'refereed_citations': ["1954PhRv...93..257G", "1954PhRv...96..730K", "1955PhRv...98...79M",
                                               "1956RScI...27..809A", "1958PhRv..112..543S", "1961RScI...32..621H"],                        
                        'reference_num': 8,
                        'rn_citations':  0.693503,
                        'rn_citations_hist':
                        {"1992": 0.6800104945559491, "1961": 0.6003174603174604, 
                         "1963": 0.6717460317460318, "1955": 0.3380952380952381}
                        }
        m = MetricsRecord(**metrics_data)
        for key in metrics_data:
            self.assertEqual(getattr(m, key), metrics_data[key], '{} field failed'.format(key))
    
    def test_time(self):
        """protobuf time field requires conversion back to python datetime"""
        test_datetime = datetime.now()
        time.sleep(.01)  # just incase some other code is doing datetime.now() and using that timestamp 
        metrics_data = {'bibcode': '1954PhRv...93..256R', 
                        'modtime': test_datetime}
        m = MetricsRecord(**metrics_data)
        m_iso = m.modtime.ToJsonString()
        m_datetime = datetime.strptime(m_iso, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.assertEqual(test_datetime, m_datetime)
    
    def test_id(self):
        """id field is not serialized, when present it should not raise exception"""
        metrics_data = {'bibcode': '1954PhRv...93..256R', 
                        'id': 1}
        m = MetricsRecord(**metrics_data)
        m_id = getattr(m, 'id', None)
        self.assertEqual(None, m_id)

      
    def test_rn_citation_data(self):
        """rn_citation_data list is converted to protobuf citation_record list"""
        metrics_data = {'bibcode': '1954PhRv...93..256R', 
                        'rn_citation_data':
                        [{"ref_norm": 0.2, "pubyear": 1954, "auth_norm": 0.25, 
                          "bibcode": "1954PhRv...93..257G", "cityear": 1954},
                         {"ref_norm": 0.07142857142857142, "pubyear": 1954, "auth_norm": 0.25, 
                          "bibcode": "1954PhRv...96..730K", "cityear": 1954}, 
                         {"ref_norm": 0.06666666666666667, "pubyear": 1954, "auth_norm": 0.25, 
                          "bibcode": "1955PhRv...98...79M", "cityear": 1955}]}                       
        m = MetricsRecord(**metrics_data)
        
        t = metrics_data['rn_citation_data']  # test data
        p = m.rn_citation_data  # protobuf data
        self.assertEqual(len(t), len(p))
        for i in range(0, len(t)):
            for key in t[i]:
                self.assertEqual(t[i][key], getattr(p[i], key), 'rn_citation_data field {}'.format(key))

                        

if __name__ == '__main__':
    unittest.main()
