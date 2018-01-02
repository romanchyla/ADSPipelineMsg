
import unittest
from adsmsg import msg

from adsmsg.nonbibrecord import NonBibRecord, DataLinksRecord

class TestMsg(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_nonbib(self):
        """test creation of protobuf 

        should include at least all fields listed AdsDataSqlSync:adsdata/run.py:nonbib_to_master_fields"""
        nonbib_data = {'bibcode': '2003ASPC..295..361M', 
                       'boost': 3.1,
                       'citation_count': 3,
                       'data': ['NED:15', 'CDS:5'],
                       'data_links_rows': [{'link_type': 'a', 'link_sub_type': 'b', 
                                            'url': ['http://a', 'http://b'],
                                            'title': ['x', 'y'],
                                            'item_count':1},
                                           {'link_type': 'aa', 'link_sub_type': 'bb', 
                                            'url': ['http://aa', 'http://bb'],
                                            'title': ['xx', 'yy'],
                                            'item_count':2}],
                       'esource': ['a', 's', 'd', 'f'],
                       'grants': ['g1', 'g2'],
                       'ned_objects': ['ned1', 'ned2'],
                       'norm_cites': 2,
                       'read_count': 7,
                       'readers': ['r1', 'r2'],
                       'reference': ['ref1', 'ref2'],
                       'simbad_objects': ['s1', 's2'],
                       'total_link_counts': 20
                       }
        m = NonBibRecord(**nonbib_data)
        self.assertEqual(m.bibcode, nonbib_data['bibcode'])
        self.assertAlmostEqual(m.boost, nonbib_data['boost'], places=5)
        self.assertEqual(m.citation_count, nonbib_data['citation_count'])
        self.assertEqual(m.esource, nonbib_data['esource'])
        self.assertEqual(m.grants, nonbib_data['grants'])
        self.assertEqual(m.ned_objects, nonbib_data['ned_objects'])
        self.assertEqual(m.norm_cites, nonbib_data['norm_cites'])
        self.assertEqual(m.read_count, nonbib_data['read_count'])
        self.assertEqual(m.readers, nonbib_data['readers'])
        self.assertEqual(m.reference, nonbib_data['reference'])
        self.assertEqual(m.simbad_objects, nonbib_data['simbad_objects'])
        self.assertEqual(m.total_link_counts, nonbib_data['total_link_counts'])
        self.assertEqual(m.data.data, nonbib_data['data']) # data is a special field name

        for i in range(len(nonbib_data['data_links_rows'])):
            self.assertEqual(m.data_links_rows[i].link_type, nonbib_data['data_links_rows'][i]['link_type'])
            self.assertEqual(m.data_links_rows[i].link_sub_type, nonbib_data['data_links_rows'][i]['link_sub_type'])
            self.assertEqual(m.data_links_rows[i].url, nonbib_data['data_links_rows'][i]['url'])
            self.assertEqual(m.data_links_rows[i].title, nonbib_data['data_links_rows'][i]['title'])
            self.assertEqual(m.data_links_rows[i].item_count, nonbib_data['data_links_rows'][i]['item_count'])


    def test_datalinks(self):
        """test creation of protobuf

        should include at least all fields listed AdsDataSqlSync:adsdata/run.py:nonbib_to_master_fields"""
        datalinks_data = {'bibcode': '2003ASPC..295..361M',
                          'data_links_rows': [{'link_type': 'a', 'link_sub_type': 'b',
                                               'url': ['http://a', 'http://b'],
                                               'title': ['x', 'y'],
                                               'item_count':1},
                                              {'link_type': 'aa', 'link_sub_type': 'bb',
                                               'url': ['http://aa', 'http://bb'],
                                               'title': ['xx', 'yy'],
                                               'item_count':2}]
                          }
        m = DataLinksRecord(**datalinks_data)
        self.assertEqual(m.bibcode, datalinks_data['bibcode'])

        for i in range(len(datalinks_data['data_links_rows'])):
            self.assertEqual(m.data_links_rows[i].link_type, datalinks_data['data_links_rows'][i]['link_type'])
            self.assertEqual(m.data_links_rows[i].link_sub_type, datalinks_data['data_links_rows'][i]['link_sub_type'])
            self.assertEqual(m.data_links_rows[i].url, datalinks_data['data_links_rows'][i]['url'])
            self.assertEqual(m.data_links_rows[i].title, datalinks_data['data_links_rows'][i]['title'])
            self.assertEqual(m.data_links_rows[i].item_count, datalinks_data['data_links_rows'][i]['item_count'])


if __name__ == '__main__':
    unittest.main()
