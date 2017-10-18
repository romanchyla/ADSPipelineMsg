
import unittest
from adsmsg import msg

from adsmsg.nonbibrecord import NonBibRecord

class TestMsg(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test(self):
        nonbib_data = {'bibcode': '2003ASPC..295..361M', 
                       'boost': 3.1,
                       'total_link_counts': 20,
                       'esource': ['a', 's', 'd', 'f'],
                       'data': ['NED:15', 'CDS:5'],
                       'data_links_rows': [{'link_type': 'a', 'link_sub_type': 'b', 
                                            'url': ['http://a', 'http://b'],
                                            'title': ['x', 'y'],
                                            'item_count':1},
                                           {'link_type': 'aa', 'link_sub_type': 'bb', 
                                            'url': ['http://aa', 'http://bb'],
                                            'title': ['xx', 'yy'],
                                            'item_count':2}],
                       }
        m = NonBibRecord(**nonbib_data)
        self.assertEqual(m.bibcode, nonbib_data['bibcode'])
        self.assertAlmostEqual(m.boost, nonbib_data['boost'], places=5)
        self.assertEqual(m.total_link_counts, nonbib_data['total_link_counts'])
        self.assertEqual(m.data.data, nonbib_data['data']) # data is a special field name
        self.assertEqual(m.esource, nonbib_data['esource'])
        for i in range(len(nonbib_data['data_links_rows'])):
            self.assertEqual(m.data_links_rows[i].link_type, nonbib_data['data_links_rows'][i]['link_type'])
            self.assertEqual(m.data_links_rows[i].link_sub_type, nonbib_data['data_links_rows'][i]['link_sub_type'])
            self.assertEqual(m.data_links_rows[i].url, nonbib_data['data_links_rows'][i]['url'])
            self.assertEqual(m.data_links_rows[i].title, nonbib_data['data_links_rows'][i]['title'])
            self.assertEqual(m.data_links_rows[i].item_count, nonbib_data['data_links_rows'][i]['item_count'])



if __name__ == '__main__':
    unittest.main()
