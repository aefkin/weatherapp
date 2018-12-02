"""
Parser test case.
"""
import json
import unittest

from weatherapp import parser


class ParserTestCase(unittest.TestCase):

    def setUp(self):
        handler = open("test_results.json")
        self.test_results = json.loads(handler.read())
        handler.close()

    def test_parse_location_data(self):
        self.assertEqual(
            (2988507, "Paris", "FR",),
            parser.Parser().parse_location_data(self.test_results),
        )

    def test_parse_forecasting_data_result_keys(self):
        forecasting_data = parser.Parser().parse_forecasting_data(
            self.test_results
        )
        for key in ("timestamp", "main", "weather"):
            for data in list(forecasting_data):
                self.assertIn(key, data)

    def test_parse_storage_data_length(self):
        self.assertEqual(
            len(self.test_results.get("list")),
            len(parser.Parser().parse_storage_data(self.test_results)),
        )
