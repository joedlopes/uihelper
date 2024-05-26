#
# Author: Joed Lopes da Silva
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.


import pyqtgraph.opengl as pgl
import numpy as np


class PCLViewWidget(pgl.GLViewWidget):
    """
    Point Cloud visualization.
    Use the *draw* (Draw3D) to draw points and lines.
    """

    def __init__(self) -> None:
        super().__init__()

        self.grid: pgl.GLGridItem = pgl.GLGridItem()

        self.scatter: pgl.GLScatterPlotItem = pgl.GLScatterPlotItem(
            pos=np.ones((0, 3)), color=(0, 1, 0, 0), size=0.05, pxMode=False
        )
        self.line_plot: pgl.GLLinePlotItem = pgl.GLLinePlotItem(
            antialias=True, mode="lines", width=1
        )

        self.addItem(self.grid)
        self.addItem(self.scatter)
        self.addItem(self.line_plot)

        from ..helpers.draw_helper_pyqtgraph import Draw3D

        self.draw = Draw3D(self.scatter, self.line_plot, self)
        self.draw.reset()
