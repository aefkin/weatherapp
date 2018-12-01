"""
Handlers module.
"""
import time
import _thread

from gi.repository import Gtk


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

    def _start_loading(self, button):
        """
        Start loading state.
        """
        button.set_sensitive(False)
        self._start_spinner()

    def _stop_loading(self, button):
        """
        Fire up search and stop loading state.
        """
        time.sleep(3)
        self._stop_spinner()
        button.set_sensitive(True)

    def on_destroy(self, *args):
        """
        Quit application
        """
        Gtk.main_quit()

    def on_search_location_clicked(self, button):
        """
        Search location handlers.
        """
        self._start_loading(button)
        _thread.start_new_thread(self._stop_loading, (button,))
