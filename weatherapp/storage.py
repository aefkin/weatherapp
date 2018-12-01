"""
Storage related operations module.
"""
import os
import pickle


class Location():
    """
    Define a location
    """
    def __init__(self, identifier, name, country):
        self.measurements = []
        self.identifier = identifier
        self.name = name
        self.conutry = country

    @staticmethod
    def pickle_file_name(identifier, name, country):
        """
        Prepare a filename for storage.
        """
        return "{}.{}.{}.pkl".format(
            identifier,
            name,
            country,
        )

    def add_measurement(self, measurement):
        """
        Add a new measurement or update and older one based on posix time.
        """
        timestamps = list(map(lambda x: x.get("dt"), self.measurements))
        self.measurements[:] = list(
            filter(
                lambda x: x.get("dt") != measurement.get("dt"),
                self.measurements,
            )
        )
        self.measurements.append(measurement)
        self.measurements = sorted(self.measurements, key=lambda x: x["dt"])


class Storage():
    """
    Storage operator.
    """
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

    def _prepare_path(self, filename):
        """
        Build storage path for specific file.
        """
        return os.path.join(self.base_dir, filename)
    
    def load_location(self, filename):
        """
        Load a location from storage.
        """
        path = self._prepare_path(filename)
        try:
            location = pickle.load(open(path, "rb"))
            return location
        except Exception as error:
            return None

    def save_location(self, filename, location):
        """
        Save a location from storage.
        """
        path = self._prepare_path(filename)
        pickle.dump(
            location,
            open(path, "wb"),
            protocol=pickle.HIGHEST_PROTOCOL
        )
