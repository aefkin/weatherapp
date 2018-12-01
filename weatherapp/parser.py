"""
Parsing related operations module.
"""
class Parser():
    """
    Parser for search results.
    """
    @staticmethod
    def parse_city_data(results):
        """
        Gather the internal OWM city ID, the name and the country code.
        """
        city = results.get("city", {})
        return city.get("id"), city.get("name"), city.get("country")

    @staticmethod
    def parse_forecasting_data(results):
        """
        Parse results for forecasting section.
        """
        measurements = results.get("list")
        forecasting_data = map(
            lambda x: {
                "timestamp": x.get("dt_txt"),
                "main": x.get("main"),
                "weather": x.get("weather"),
            },
            measurements,
        )
        return forecasting_data
