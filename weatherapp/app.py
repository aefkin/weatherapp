"""
WeatherApp Application.
"""
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gio
from gi.repository import Gtk

from . import handlers
from . import window


class App(Gtk.Application):
    """
    Application definition.
    """
    def __init__(self):
        Gtk.Application.__init__(
            self,
            application_id="org.gnome.weatherapp",
            flags=Gio.ApplicationFlags.FLAGS_NONE,
        )
        self._window = None

    def do_startup(self):
        """
        Startup signal handler.
        """
        Gtk.Application.do_startup(self)
        self._builder = Gtk.Builder()
        self._builder.add_from_file("ui.glade")
        self._builder.connect_signals(handlers.Handler())


    def do_activate(self):
        """
        Activate signal handler
        """
        if not self._window:
            app_window = self._prepare_app_window()
            self._window = app_window
        self._window.present()

    def _prepare_app_window(self):
        """
        Prepare window from glade to be used in application.
        """
        app_window = self._builder.get_object("weatherapp")
        app_window.set_application(self)
        return app_window


def main():
    app = App()
    app.run(None)


if __name__ == "__main__":
    main()
