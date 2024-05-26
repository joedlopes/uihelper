#
# Author: Joed Lopes da Silva
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

from typing import Dict, Union
import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QColor,
    QBrush,
    QPainter,
    QPixmap,
    QImage,
    QMouseEvent,
    QWheelEvent,
)
from PySide6.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsPixmapItem,
)
from PySide6.QtOpenGLWidgets import QOpenGLWidget


class ImageViewWidget(QGraphicsView):
    def __init__(self) -> None:
        QGraphicsView.__init__(self)

        self.left_button: Dict[str, Union[bool, int, float]] = {
            "pressed": False,
            "xi": 0,
            "yi": 0,
            "x0": 0,
            "y0": 0,
        }
        self.mid_button: Dict[str, Union[bool, int, float]] = {
            "pressed": False,
            "xi": 0,
            "yi": 0,
            "x0": 0,
            "y0": 0,
        }

        self.setViewport(QOpenGLWidget())
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.SmartViewportUpdate)
        self.setBackgroundBrush(QBrush(QColor(0, 0, 0)))
        self.setMouseTracking(True)
        self.setCacheMode(QGraphicsView.CacheModeFlag.CacheBackground)
        self.setRenderHints(
            QPainter.RenderHint.Antialiasing
            | QPainter.RenderHint.TextAntialiasing
            | QPainter.RenderHint.SmoothPixmapTransform
        )

        self._scene: QGraphicsScene = QGraphicsScene()
        self.image_item: QGraphicsPixmapItem = QGraphicsPixmapItem()

        self._scene.addItem(self.image_item)
        self.setScene(self._scene)

        self.update()

    def set_image(self, image: np.ndarray) -> None:
        if image is None:
            self.set_image_pixmap(None)
            return

        h, w = image.shape[0], image.shape[1]
        d = 1
        if len(image.shape) > 2 and image.shape[2] >= 3:
            d = image.shape[2]

        bpl = w * d
        img = QImage(
            image.data,
            w,
            h,
            bpl,
            QImage.Format.Format_RGB888 if d > 1 else QImage.Format.Format_Indexed8,
        )
        self.set_image_pixmap(QPixmap.fromImage(img))
        del image
        del img

    def set_image_pixmap(self, qpixmap: QPixmap) -> None:
        if qpixmap is None:
            self.image_item.setPixmap(QPixmap())
        else:
            image, self.w, self.h = qpixmap, qpixmap.width(), qpixmap.height()
            self.image_item.setPixmap(image)
            self._scene.setSceneRect(0, 0, self.w, self.h)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        p = self.mapToScene(ev.pos())

        if ev.button() == Qt.MouseButton.LeftButton:
            self.left_button["pressed"] = True
            self.left_button["xi"] = p.x()
            self.left_button["yi"] = p.y()
            self.left_button["x0"] = p.x()
            self.left_button["y0"] = p.y()

        if ev.button() == Qt.MouseButton.MiddleButton:
            self.mid_button["pressed"] = True
            self.mid_button["xi"] = p.x()
            self.mid_button["yi"] = p.y()
            self.mid_button["x0"] = p.x()
            self.mid_button["y0"] = p.y()

        QGraphicsView.mousePressEvent(self, ev)

    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        if self.mid_button["pressed"]:
            self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
            self.translate(1, 1)

        QGraphicsView.mouseMoveEvent(self, ev)

    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        if ev.button() == Qt.MouseButton.LeftButton:
            if self.left_button["pressed"]:
                self.left_button["pressed"] = False

        if ev.button() == Qt.MouseButton.MiddleButton:
            if self.mid_button["pressed"]:
                self.mid_button["pressed"] = False

        QGraphicsView.mouseReleaseEvent(self, ev)

    def wheelEvent(self, event: QWheelEvent) -> None:
        zoom_in_factor = 1.25
        zoom_out_factor = 1 / zoom_in_factor

        pos_x, pos_y = int(event.position().x()), int(event.position().y())

        old_pos = self.mapToScene(pos_x, pos_y)
        if event.angleDelta().y() > 0:
            zoom_factor = zoom_in_factor
        else:
            zoom_factor = zoom_out_factor
        self.scale(zoom_factor, zoom_factor)

        pos_x, pos_y = int(event.position().x()), int(event.position().y())
        new_pos = self.mapToScene(pos_x, pos_y)
        delta = new_pos - old_pos
        self.translate(delta.x(), delta.y())

    def zoom_out(self) -> None:
        self.scale(0.20, 0.2)

    def fit_to_image(self) -> None:
        self.centerOn(self.image_item)
        self.fitInView(
            self.image_item.boundingRect(), Qt.AspectRatioMode.KeepAspectRatio
        )
