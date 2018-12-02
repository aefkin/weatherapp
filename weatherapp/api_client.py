"""
OpenWeatherMap API client.
"""
from requests.exceptions import HTTPError
import requests

from . import constants


class OWMClient():
    """
    REST Client for OWM API.
    """
    def __init__(self):
        self.base_url = "https://api.openweathermap.org/data/2.5/"

    def _check_for_valid_response(self, response):
        """
        Return the JSON response if request has succeeded.
        Else returns None.
        """
        try:
            response.raise_for_status()
        except HTTPError as error:
            return None
        else:
            return response.json()

    def forecast(self, city, country_code):
        """
        Consume forecasting endpoint.
        """
        resp = requests.get(
            self.base_url + \
            "forecast?appid=" + constants.OWM_API_KEY + \
            "&q=" + city + "," + country_code.upper() + \
            "&units=metric",
            timeout=constants.OWM_API_CLIENT_TIMEOUT,
        )
        return self._check_for_valid_response(resp)
