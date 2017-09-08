import sys
import os

import unittest
from adsmsg import CitationChanges, CitationChange, Status


class TestCitationChanges(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.proj_home = os.path.join(os.path.dirname(__file__), '../..')


    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_is_valid(self):
        citation_changes = CitationChanges()
        citation_change = citation_changes.changes.add()
        citation_change.citing = "1005PhRvC..71c4906H"
        citation_change.cited = "1976NuPhB.113..395J"
        citation_change.doi = "10.1016/0550-3213(76)90133-4"
        citation_change.pid = ""
        citation_change.url = ""
        citation_change.score = "1"
        citation_change.status = Status.new
        citation_change = citation_changes.changes.add()
        citation_change.citing = "2017SSEle.128..141M"
        citation_change.cited = "..................."
        citation_change.doi = ""
        citation_change.pid = ""
        citation_change.url = "https://github.com/viennats/viennats-dev"
        citation_change.score = "0"
        citation_change.status = Status.new
        citation_change = citation_changes.changes.add()
        citation_change.citing = "2017PASP..129b4005R"
        citation_change.cited = "2013ascl.soft03021B"
        citation_change.doi = ""
        citation_change.pid = "ascl:1303.021"
        citation_change.url = ""
        citation_change.score = "1"
        citation_change.status = Status.new
        self.assertTrue(citation_changes.is_valid())

    def test_individual_is_valid(self):
        citation_change = CitationChange(citing= "1005PhRvC..71c4906H", cited= "1976NuPhB.113..395J", doi='10.1016/0550-3213(76)90133-4', score='1', status='new')
        self.assertTrue(citation_change.is_valid())
        self.assertEqual(citation_change.citing, "1005PhRvC..71c4906H")
        self.assertEqual(citation_change.cited, "1976NuPhB.113..395J")
        self.assertEqual(citation_change.doi, "10.1016/0550-3213(76)90133-4")
        self.assertEqual(citation_change.pid, "")
        self.assertEqual(citation_change.url, "")
        self.assertEqual(citation_change.score, "1")
        self.assertEqual(citation_change.status, Status.new)


if __name__ == '__main__':
    unittest.main()
