"""
Search related operations module.
"""
import json

from . import api_client


class Searcher():
    """
    Operations around searching a forecast.
    """
    @staticmethod
    def _get_response(city, country_code):
        """
        Actual call to OWM API.
        """
        return api_client.OWMClient().forecast(city, country_code)

    def search(self, city, country_code):
        """
        Perform forecast search and return results.
        """
        response = self._get_response(city, country_code)
        if response is None:
            return None
        return response
