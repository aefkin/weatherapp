"""
Handlers module.
"""
from gi.repository import Gtk


class Handler():
    """
    Handlers collection.
    """
    def on_destroy(self, *args):
        """
        Quit application
        """
        Gtk.main_quit()


