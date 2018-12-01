"""
Search related operations module.
"""
import json

# from . import api_client


class Searcher():
    """
    Operations around searching a forecast.
    """
    # @staticmethod
    # def _get_response(city, country_code):
    #     """
    #     Actual call to OWM API.
    #     """
    #     return api_client.OWMClient().forecast(city, country_code)

    @staticmethod
    def _get_fake_response():
        with open("test_results.json") as handler:
            text = handler.read()
        return json.loads(text)

    def search(self, city, country_code):
        """
        Perform forecast search and return results.
        """
        # TODO: replace next line with following comment
        # response = self._get_response(city, country_code)
        response = self._get_fake_response()
        if response is None:
            return None
        return response
