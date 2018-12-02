"""
Simple plotting module.

Inspired by: 
https://gtk3-matplotlib-cookbook.readthedocs.io/en/latest/hello-plot.html
"""
from matplotlib.figure import Figure


class Plotter():
    """
    Plot generator.
    """
    def __init__(self, measurements):
        self.min_data = self._prepare_data_object_for_key(
            measurements,
            "temp_min",
        )
        self.max_data = self._prepare_data_object_for_key(
            measurements,
            "temp_max",
        )
        self.n_cols = len(measurements)
        self.n_rows = 20  # determine me
        self.figure = Figure(figsize=(5, 5), dpi=100)

    def _prepare_data_object_for_key(self, measurements, key):
        """
        Transform measurements into something plottable.
        """
        return {
                "temp": [measurement["main"][key] for measurement in measurements],
                "date": [measurement["dt_txt"] for measurement in measurements],
        }

    def _prepare_axes(self):
        """
        Generate subplot axes.
        """
        axes = self.figure.add_subplot(111)
        return axes

    def _plot(self):
        """
        Prepare graph lines.
        """
        axes = self._prepare_axes()

        axes.plot("date", "temp", data=self.min_data)
        axes.plot("date", "temp", data=self.max_data)

        axes.tick_params(axis='x', rotation=-70)

    @property
    def plot(self):
        """
        Return actual plot.
        """
        self._plot()
        return self.figure
