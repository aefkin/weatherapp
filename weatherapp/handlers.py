"""
Handlers module.
"""
from gi.repository import Gtk

from . import search
from . import parser


class Handler():
    """
    Handlers collection.
    """
    def __init__(self, builder):
        self._builder = builder

    def _start_spinner(self):
        """
        Activate spinning.
        """
        spinner = self._builder.get_object("search_spinner")
        spinner.start()

    def _stop_spinner(self):
        """
        Stop spinning.
        """
        spinner = self._builder.get_object("search_spinner")
        spinner.stop()

    def _start_loading(self):
        """
        Start loading state.
        """
        city_location = self._builder.get_object("city_location")
        city_location.set_sensitive(False)
        country_location = self._builder.get_object("country_location")
        country_location.set_sensitive(False)
        button = self._builder.get_object("search_location")
        button.set_sensitive(False)
        self._start_spinner()

    def _stop_loading(self):
        """
        Fire up search and stop loading state.
        """
        results = self._start_searching()
        self._stop_searching(results)
        self._stop_spinner()
        button = self._builder.get_object("search_location")
        button.set_sensitive(True)
        city_location = self._builder.get_object("city_location")
        city_location.set_sensitive(True)
        country_location = self._builder.get_object("country_location")
        country_location.set_sensitive(True)

    def _start_searching(self):
        """
        Start search operations.
        """
        city, country_code = self._get_city_and_country()
        results = search.Searcher().search(city, country_code)
        if results is None:
            return None
        return results

    def _stop_searching(self, results):
        """
        Process search results.
        """
        if results is None:
            return
        forecasting_data = parser.Parser().parse_forecasting_data(results)
        self._draw_forecasting_data(forecasting_data)

    def _get_city_and_country(self):
        """
        Retrieve city name and country code from search widgets.
        """
        city_location = self._builder.get_object("city_location")
        country_location = self._builder.get_object("country_location")
        return city_location.get_text(), country_location.get_text()

    def _draw_forecast_box(self, forecast):
        """
        Draw a forecast box.
        """
        forecasting_box = self._builder.get_object("forecasting_box")

        forecast_box = Gtk.ListBox()
        forecast_box.set_selection_mode(Gtk.SelectionMode.NONE)

        date, hour = forecast.get("timestamp").split(" ")

        date_label = Gtk.Label(date)
        date_label.set_justify(Gtk.Justification.CENTER)
        forecast_box.add(date_label)

        hour_label = Gtk.Label(hour)
        hour_label.set_justify(Gtk.Justification.CENTER)
        forecast_box.add(hour_label)

        weather_label = Gtk.Label(forecast.get("weather")[0].get("description"))
        weather_label.set_justify(Gtk.Justification.CENTER)
        forecast_box.add(weather_label)

        maxtemp_label = Gtk.Label(
            str(forecast.get("main").get("temp_max")) + " ºC"
        )
        maxtemp_label.set_justify(Gtk.Justification.CENTER)
        forecast_box.add(maxtemp_label)

        mintemp_label = Gtk.Label(
            str(forecast.get("main").get("temp_min")) + " ºC"
        )
        mintemp_label.set_justify(Gtk.Justification.CENTER)
        forecast_box.add(mintemp_label)

        humidity_label = Gtk.Label(
            str(forecast.get("main").get("humidity")) + " %"
        )
        humidity_label.set_justify(Gtk.Justification.CENTER)
        forecast_box.add(humidity_label)

        forecasting_box.add(forecast_box)
        forecast_box.show_all()

    def _draw_forecasting_data(self, forecasting_data):
        """
        Update the forecasting box with search results.
        """
        for forecast in forecasting_data:
            self._draw_forecast_box(forecast)

    def on_destroy(self, *args):
        """
        Quit application
        """
        Gtk.main_quit()

    def on_search_location_clicked(self, *args):
        """
        Search location handlers.
        """
        if not all(self._get_city_and_country()):
            return
        self._start_loading()
        self._stop_loading()
