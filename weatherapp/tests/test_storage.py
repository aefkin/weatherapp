"""
Storage module test cases.
"""
import unittest
import os

from weatherapp import storage


class LocationTestCase(unittest.TestCase):

    def setUp(self):
        self.test_location = storage.Location(123456, "city", "CC")

    def test_pickle_file_name(self):
        self.assertEqual(
            "123456.city.CC.pkl",
            storage.Location.pickle_file_name(
                123456,
                "city",
                "CC",
            )
        )

    def test_add_measurement(self):
        measurement = {
            "dt": 1544108400,
            "main": {},
            "weather": [{}],
            "dt_txt": "2018-12-06 15:00:00",
        }
        self.test_location.add_measurement(measurement)
        self.assertIn(
            measurement,
            self.test_location.measurements
        )


class StorageTestCase(unittest.TestCase):

    def setUp(self):
        self.test_storage = storage.Storage()
        self.test_filename = "test.pkl"
        self.test_location =  storage.Location(123456, "city", "CC")

    def test_prepare_path(self):
        self.assertEqual(
            self.test_storage._prepare_path(self.test_filename),
            os.path.join(self.test_storage.base_dir, self.test_filename),
        )

    def test_load_location_returns_none(self):
        self.assertIsNone(
            self.test_storage.load_location(self.test_filename)
        )

    def test_load_location_returns_location(self):
        self.test_storage.save_location(self.test_filename, self.test_location)
        self.assertIsInstance(
            self.test_storage.load_location(self.test_filename),
            storage.Location,
        )
        os.remove(self.test_storage._prepare_path(self.test_filename))

