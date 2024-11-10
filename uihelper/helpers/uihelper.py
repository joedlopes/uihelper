#
# Author: Joed Lopes da Silva
# This library is licensed under MIT License
#
# Copyright Joed 2023
#
from functools import wraps
from typing import (
    List,
    Tuple,
    Union,
    Optional,
    Sequence,
    Final,
    Callable,
    TypeVar,
    Any,
    Dict,
    cast,
    Literal,
)
import os
import logging
from datetime import datetime
from enum import Enum

from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6 import QtCore


from PySide6.QtWidgets import (
    QPushButton,
    QToolButton,
    QWidget,
    QApplication,
    QLineEdit,
    QLabel,
    QTextEdit,
    QTabWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QScrollArea,
    QMainWindow,
    QLayout,
    QDockWidget,
    QMenu,
    QMenuBar,
    QToolBar,
    QStatusBar,
    QCheckBox,
    QRadioButton,
    QTreeWidget,
    QTreeWidgetItem,
    QSpinBox,
    QDoubleSpinBox,
    QFrame,
    QMessageBox,
    QErrorMessage,
    QColorDialog,
    QFileDialog,
    QComboBox,
    QSlider,
    QSpacerItem,
    QStackedWidget,
    QSizePolicy,
    QSplitter,
    QListView,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QGroupBox,
    QItemDelegate,
)

from PySide6.QtGui import (
    QIcon,
    QAction,
    QColor,
    QPixmap,
    QPainter,
    QFont,
    QFontDatabase,
    QKeySequence,
)

from PySide6.QtCore import (
    Slot,
    Qt,
    QSize,
    Signal,
    QObject,
    QKeyCombination,
    QCoreApplication,
    QTimer,
)


__all__ = [
    # QT
    "Qt",
    "QtWidgets",
    "QtGui",
    "QtCore",
    "QFont",
    "QObject",
    "QApplication",
    "QWidget",
    "QMainWindow",
    "QCoreApplication",
    "QFontDatabase",
    "Signal",
    "Slot",
    "QObject",
    "QHeaderView",
    "QAbstractItemView",
    "QTabWidget",
    "QKeySequence",
    # Library Components
    "Button",
    "ToolButton",
    "Label",
    "ComboBox",
    "TextEdit",
    "SpinBox",
    "DoubleSpinBox",
    "LineEdit",
    "CheckBox",
    "RadioButton",
    "ListView",
    "TableWidgetItem",
    "TableWidget",
    "TreeWidget",
    "TreeWidgetItem",
    "PixmapM",
    "IconM",
    "Action",
    "Menu",
    "MenuBar",
    "ToolBarNextLine",
    "ToolBar",
    "StatusBar",
    "DockWidget",
    "DockWidgetSized",
    "Splitter",
    "SpacerItem",
    "VSpacer",
    "HSpacer",
    "ScrollArea",
    "Align",
    "set_layout_props",
    "VBox",
    "HBox",
    "NextColumn",
    "NextRow",
    "AddStretch",
    "AddStretchLayout",
    "Columns",
    "Rows",
    "set_uniform_label_width",
    "Form",
    "GroupBox",
    "Frame",
    "HLine",
    "StackedWidget",
    "Widget",
    "MainWindow",
    "Alert",
    "Error",
    "Confirm",
    "Color",
    "OpenFile",
    "OpenFiles",
    "SaveFile",
    "OpenDir",
    "ApplicationContext",
    "Application",
    "app_set_font",
    "Timer",
]

# Size properties


class SizePolicy:
    Expanding: Final = QSizePolicy.Policy.Expanding
    Maximum: Final = QSizePolicy.Policy.Maximum
    Minimum: Final = QSizePolicy.Policy.Minimum
    Preferred: Final = QSizePolicy.Policy.Preferred
    Fixed: Final = QSizePolicy.Policy.Fixed


class DockArea:
    Left: Final = Qt.DockWidgetArea.LeftDockWidgetArea
    Right: Final = Qt.DockWidgetArea.RightDockWidgetArea
    Top: Final = Qt.DockWidgetArea.TopDockWidgetArea
    Bottom: Final = Qt.DockWidgetArea.BottomDockWidgetArea
    All: Final = Qt.DockWidgetArea.AllDockWidgetAreas
    No: Final = Qt.DockWidgetArea.NoDockWidgetArea


# Decorator for Window Properties

DecoratorFunction = TypeVar("DecoratorFunction", bound=Callable[..., Any])


def window_ops_set(func: DecoratorFunction) -> DecoratorFunction:
    @wraps(func)
    def wrapper(*args, **kwargs):
        widget = func(*args, **kwargs)
        window_size = kwargs.get("window_size")
        window_title = kwargs.get("window_title")

        if window_size is not None:
            if not isinstance(window_size, tuple) or len(window_size) != 2:
                raise TypeError("window_size must be a tuple of two integers")
            if any(not isinstance(dim, int) or dim <= 0 for dim in window_size):
                raise ValueError("Both dimensions in size must be positive integers")
            widget.resize(*window_size)

        if window_title is not None:
            if not isinstance(window_title, str):
                raise TypeError("title must be a string")
            widget.setWindowTitle(window_title)

        return widget

    return cast(DecoratorFunction, wrapper)


# Decorators for setting widget properties


def set_widget_size(func: DecoratorFunction) -> DecoratorFunction:
    @wraps(func)
    def wrapper(*args, **kwargs):
        widget = func(*args, **kwargs)
        min_width = kwargs.get("min_width")
        max_width = kwargs.get("max_width")
        min_height = kwargs.get("min_height")
        max_height = kwargs.get("max_height")

        if min_width is not None:
            if not isinstance(min_width, int) or min_width < 0:
                raise ValueError("min_width must be a non-negative integer")
            widget.setMinimumWidth(min_width)
        if max_width is not None:
            if not isinstance(max_width, int) or max_width < 0:
                raise ValueError("max_width must be a non-negative integer")
            widget.setMaximumWidth(max_width)
        if min_height is not None:
            if not isinstance(min_height, int) or min_height < 0:
                raise ValueError("min_height must be a non-negative integer")
            widget.setMinimumHeight(min_height)
        if max_height is not None:
            if not isinstance(max_height, int) or max_height < 0:
                raise ValueError("max_height must be a non-negative integer")
            widget.setMaximumHeight(max_height)

        if min_width is not None and max_width is not None and min_width > max_width:
            raise ValueError("min_width cannot be greater than max_width")
        if (
            min_height is not None
            and max_height is not None
            and min_height > max_height
        ):
            raise ValueError("min_height cannot be greater than max_height")

        return widget

    return cast(DecoratorFunction, wrapper)


def set_widget_object_name(func: DecoratorFunction) -> DecoratorFunction:
    @wraps(func)
    def wrapper(*args, **kwargs):
        widget = func(*args, **kwargs)
        object_name = kwargs.get("object_name")
        if object_name:
            widget.setObjectName(object_name)
        return widget

    return cast(DecoratorFunction, wrapper)


def set_widget_style_sheet(func: DecoratorFunction) -> DecoratorFunction:
    @wraps(func)
    def wrapper(*args, **kwargs):
        widget = func(*args, **kwargs)
        css = kwargs.get("css")
        if css:
            widget.setStyleSheet(css)
        return widget

    return cast(DecoratorFunction, wrapper)


def set_widget_tooltip(func: DecoratorFunction) -> DecoratorFunction:
    @wraps(func)
    def wrapper(*args, **kwargs):
        widget = func(*args, **kwargs)
        tooltip_text = kwargs.get("tooltip")
        tooltip_duration = kwargs.get("tooltip_duration_ms")
        if tooltip_text:
            widget.setToolTip(tooltip_text)
        if tooltip_duration is not None:
            widget.setToolTipDuration(tooltip_duration)
        return widget

    return cast(DecoratorFunction, wrapper)


def set_widget_shortcut(func: DecoratorFunction) -> DecoratorFunction:
    @wraps(func)
    def wrapper(*args, **kwargs):
        widget = func(*args, **kwargs)
        shortcut = kwargs.get("shortcut")
        if shortcut:
            widget.setShortcut(shortcut)
        return widget

    return cast(DecoratorFunction, wrapper)


def set_widget_icon(func: DecoratorFunction) -> DecoratorFunction:
    @wraps(func)
    def wrapper(*args, **kwargs):
        widget = func(*args, **kwargs)
        icon = kwargs.get("icon")
        icon_size = kwargs.get("icon_size")
        if icon:
            widget.setIcon(icon)
            if icon_size:
                widget.setIconSize(QSize(icon_size[0], icon_size[1]))
        return widget

    return cast(DecoratorFunction, wrapper)


def set_widget_text(func: DecoratorFunction) -> DecoratorFunction:
    @wraps(func)
    def wrapper(*args, **kwargs):
        widget = func(*args, **kwargs)
        text = kwargs.get("text")
        if text is None and len(args) > 0 and isinstance(args[0], str):
            text = args[0]

        if text is not None:
            widget.setText(text)
        return widget

    return cast(DecoratorFunction, wrapper)


def connect_slot(signal_name: str, parameter_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            widget = func(*args, **kwargs)
            slot = kwargs.get(parameter_name)
            if slot is not None:
                if not callable(slot):
                    raise TypeError(f"{parameter_name} must be a callable")
                signal = getattr(widget, signal_name)
                signal.connect(slot)
            return widget

        return wrapper

    return decorator


def set_widget_attribute(
    method_name: str,
    param_name: str,
    param_types: Union[type, Tuple[type, ...]],
    default_value: Optional[Any] = None,
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            widget = func(*args, **kwargs)
            param_value = kwargs.get(param_name, default_value)
            if param_value is not None:
                # Handle multiple parameter types
                if isinstance(param_types, tuple):
                    if not isinstance(param_value, tuple) or len(param_value) != len(
                        param_types
                    ):
                        raise TypeError(
                            f"'{param_name}' must be a tuple of {len(param_types)} elements"
                        )
                    for val, typ in zip(param_value, param_types):
                        if not isinstance(val, typ):
                            raise TypeError(
                                f"Each element in '{param_name}' must be of type {typ.__name__}"
                            )
                else:
                    if not isinstance(param_value, param_types):
                        raise TypeError(
                            f"'{param_name}' must be of type {param_types.__name__}"
                        )
                method = getattr(widget, method_name)
                if isinstance(param_value, tuple):
                    method(*param_value)
                else:
                    method(param_value)
            return widget

        return wrapper

    return decorator


def call_widget_method(method_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            widget = func(*args, **kwargs)
            method = getattr(widget, method_name)
            method()
            return widget

        return wrapper

    return decorator


def call_widget_method_with_params(
    method_name: str,
    param_name: str,
    param_types: Union[type, Tuple[type, ...]],
    default_value: Optional[Any] = None,
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            widget = func(*args, **kwargs)
            param_value = kwargs.get(param_name, default_value)
            if param_value is not None:
                # Type checking
                if isinstance(param_types, tuple):
                    if not isinstance(param_value, tuple) or len(param_value) != len(
                        param_types
                    ):
                        raise TypeError(
                            f"'{param_name}' must be a tuple of {len(param_types)} elements"
                        )
                    for val, typ in zip(param_value, param_types):
                        if not isinstance(val, typ):
                            raise TypeError(
                                f"Each element in '{param_name}' must be of type {typ.__name__}"
                            )
                else:
                    if not isinstance(param_value, param_types):
                        raise TypeError(
                            f"'{param_name}' must be of type {param_types.__name__}"
                        )
                method = getattr(widget, method_name)
                if isinstance(param_value, tuple):
                    method(*param_value)
                else:
                    method(param_value)
            return widget

        return wrapper

    return decorator


# Widgets


@set_widget_object_name
@set_widget_style_sheet
@set_widget_text
@set_widget_icon
@set_widget_shortcut
@set_widget_size
@set_widget_tooltip
@connect_slot("clicked", "on_click")
def Button(
    text: Optional[str] = None,
    *,
    widget: Optional[QPushButton] = None,
    object_name: Optional[str] = None,
    on_click: Optional[Callable[[], None]] = None,
    icon: Optional[QIcon] = None,
    icon_size: Optional[Tuple[int, int]] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
    css: Optional[str] = None,
    shortcut: Optional[str] = None,
    tooltip: Optional[str] = None,
    tooltip_duration_ms: Optional[int] = None,
) -> QPushButton:
    if widget is None:
        widget = QPushButton()

    return widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_text
@set_widget_icon
@set_widget_shortcut
@set_widget_size
@set_widget_tooltip
@set_widget_attribute("setToolButtonStyle", "button_style", Qt.ToolButtonStyle)
@connect_slot("clicked", "on_click")
def ToolButton(
    text: Optional[str] = None,
    button_style: Optional[
        Qt.ToolButtonStyle
    ] = Qt.ToolButtonStyle.ToolButtonTextUnderIcon,
    *,
    widget: Optional[QToolButton] = None,
    object_name: Optional[str] = None,
    on_click: Optional[Callable[[], None]] = None,
    icon: Optional[QIcon] = None,
    icon_size: Optional[Tuple[int, int]] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
    css: Optional[str] = None,
    shortcut: Optional[str] = None,
    tooltip: Optional[str] = None,
    tooltip_duration_ms: Optional[int] = None,
) -> QToolButton:
    if widget is None:
        widget = QToolButton()

    return widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_text
@set_widget_shortcut
@set_widget_size
@set_widget_attribute("setAlignment", "alignment", Qt.AlignmentFlag)
@set_widget_attribute("setPixmap", "pixmap", QPixmap)
@connect_slot("clicked", "on_click")
def Label(
    text: Optional[str] = None,
    *,
    widget: Optional[QLabel] = None,
    object_name: Optional[str] = None,
    css: Optional[str] = None,
    pixmap: Optional[QPixmap] = None,
    alignment: Optional[int] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
) -> QLabel:
    if widget is None:
        widget = QLabel()

    return widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_attribute("singleStep", "single_step", int)
@set_widget_attribute("value", "value", int)
@connect_slot("valueChanged", "on_value_changed")
def SpinBox(
    *,
    value_range: Optional[Tuple[int, int]] = (0, 1000),
    value: int = 1,
    single_step: int = 1,
    on_value_changed: Optional[Callable[[int], None]] = None,
    widget: Optional[QSpinBox] = None,
    object_name: Optional[str] = None,
    css: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
) -> QSpinBox:
    if widget is None:
        widget = QSpinBox()

    if value_range is not None:
        if not (isinstance(value_range, tuple) and len(value_range) == 2):
            raise ValueError("value_range must be a tuple of (min, max)")
        min_value, max_value = value_range
        if not (
            isinstance(min_value, (int, float)) and isinstance(max_value, (int, float))
        ):
            raise ValueError("min and max values in value_range must be numbers")
        if min_value > max_value:
            raise ValueError("min value cannot be greater than max value")
        widget.setRange(min_value, max_value)

    return widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_size
@connect_slot("valueChanged", "on_value_changed")
def DoubleSpinBox(
    *,
    decimals: int = 3,
    value_range: Optional[Tuple[float, float]] = (0.0, 1000.0),
    value: float = 1.0,
    single_step: float = 1.0,
    widget: Optional[QDoubleSpinBox] = None,
    on_value_changed: Optional[Callable[[float], None]] = None,
    object_name: Optional[str] = None,
    css: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
) -> QDoubleSpinBox:
    if widget is None:
        widget = QDoubleSpinBox()

    if value_range is not None:
        if not (isinstance(value_range, tuple) and len(value_range) == 2):
            raise ValueError("value_range must be a tuple of (min, max)")
        min_value, max_value = value_range
        if not (
            isinstance(min_value, (int, float)) and isinstance(max_value, (int, float))
        ):
            raise ValueError("min and max values in value_range must be numbers")
        if min_value > max_value:
            raise ValueError("min value cannot be greater than max value")
        widget.setRange(min_value, max_value)

    if decimals is not None:
        if not isinstance(decimals, int) or decimals < 0:
            raise ValueError("decimals must be a non-negative integer")
        widget.setDecimals(decimals)

    if single_step is not None:
        widget.setSingleStep(single_step)

    if value is not None:
        widget.setValue(value)

    return widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_text
@set_widget_size
@set_widget_attribute("setPlaceholderText", "placeholder_text", str)
@set_widget_attribute("setInputMask", "mask", str)
@set_widget_attribute("setReadOnly", "read_only", bool)
@connect_slot("returnPressed", "on_return_pressed")
@connect_slot("textChanged", "on_text_changed")
def LineEdit(
    text: Optional[str] = "",
    *,
    placeholder_text: Optional[str] = "",
    max_length: Optional[int] = None,
    mask: Optional[str] = None,
    on_return_pressed: Optional[Callable[[], None]] = None,
    on_text_changed: Optional[Callable[[str], None]] = None,
    widget: Optional[QLineEdit] = None,
    object_name: Optional[str] = None,
    css: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
    read_only: Optional[bool] = None,
) -> QLineEdit:
    if widget is None:
        widget = QLineEdit()

    if max_length is not None:
        if not isinstance(max_length, int) or max_length <= 0:
            raise ValueError("max_length must be a positive integer")
        widget.setMaxLength(max_length)

    return widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_text
@set_widget_icon
@set_widget_size
@connect_slot("released", "on_released")
@connect_slot("stateChanged", "on_state_changed")
def CheckBox(
    text: Optional[str] = None,
    *,
    checked: bool = False,
    on_released: Optional[Callable[[], None]] = None,
    on_state_changed: Optional[Callable[[int], None]] = None,
    widget: Optional[QCheckBox] = None,
    object_name: Optional[str] = None,
    icon: Optional[QIcon] = None,
    icon_size: Optional[Tuple[int, int]] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
    css: Optional[str] = None,
) -> QCheckBox:
    if widget is None:
        widget = QCheckBox()

    widget.setChecked(checked)

    return widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_icon
@set_widget_size
@connect_slot("currentIndexChanged", "on_index_changed")
def ComboBox(
    *,
    selected_item: Optional[str] = None,
    items: Optional[List[str]] = None,
    on_index_changed: Optional[Callable[[int], None]] = None,
    widget: Optional[QComboBox] = None,
    object_name: Optional[str] = None,
    icon: Optional[QIcon] = None,
    icon_size: Optional[Tuple[int, int]] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
    css: Optional[str] = None,
) -> QComboBox:

    if widget is None:
        widget = QComboBox()

    selected_index: int = 0
    if items:
        for i, item in enumerate(items):
            if not isinstance(item, str):
                raise ValueError("All items must be strings.")
            widget.addItem(item)
            if item == selected_item:
                selected_index = i

    widget.setCurrentIndex(selected_index)

    return widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_size
@set_widget_text
@set_widget_attribute("setPlaceholderText", "placeholder_text", str)
@connect_slot("textChanged", "on_text_changed")
def TextEdit(
    text: Optional[str] = "",
    *,
    placeholder_text: Optional[str] = "",
    on_text_changed: Optional[Callable[[], None]] = None,
    widget: Optional[QTextEdit] = None,
    object_name: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
    css: Optional[str] = None,
) -> QTextEdit:
    if widget is None:
        widget = QTextEdit()

    return widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_size
@set_widget_attribute("setOrientation", "orientation", Qt.Orientation)
@set_widget_attribute("setSingleStep", "single_step", int)
@set_widget_attribute("setPageStep", "page_step", int)
@set_widget_attribute("setValue", "value", int)
@connect_slot("valueChanged", "on_value_changed")
def Slider(
    *,
    orientation: Optional[Qt.Orientation] = Qt.Orientation.Horizontal,
    value_range: Optional[Tuple[int, int]] = (0, 100),
    value: int = 0,
    single_step: int = 1,
    page_step: int = 10,
    on_value_changed: Optional[Callable[[int], None]] = None,
    widget: Optional[QSlider] = None,
    object_name: Optional[str] = None,
    css: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
) -> QSlider:
    if widget is None:
        widget = QSlider()

    if value_range is not None:
        if not (isinstance(value_range, tuple) and len(value_range) == 2):
            raise ValueError("value_range must be a tuple of (min, max)")
        min_value, max_value = value_range
        if not (isinstance(min_value, int) and isinstance(max_value, int)):
            raise ValueError("min and max values in value_range must be integers")
        if min_value > max_value:
            raise ValueError("min value cannot be greater than max value")
        widget.setRange(min_value, max_value)

    return widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_text
@set_widget_icon
@set_widget_size
@set_widget_attribute("setChecked", "checked", bool)
@connect_slot("released", "on_released")
@connect_slot("toggled", "on_toggled")
def RadioButton(
    text: Optional[str] = None,
    *,
    checked: bool = False,
    on_released: Optional[Callable[[], None]] = None,
    on_toggled: Optional[Callable[[bool], None]] = None,
    widget: Optional[QRadioButton] = None,
    object_name: Optional[str] = None,
    icon: Optional[QIcon] = None,
    icon_size: Optional[Tuple[int, int]] = None,
    css: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
) -> QRadioButton:
    if widget is None:
        widget = QRadioButton()
    return widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_size
def ListView(
    *,
    widget: Optional[QListView] = None,
    object_name: Optional[str] = None,
    css: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
) -> QListView:
    if widget is None:
        widget = QListView()
    return widget


@set_widget_text
def TableWidgetItem(
    text: Optional[str] = None,
    *,
    widget: Optional[QTableWidgetItem] = None,
) -> QTableWidgetItem:
    if widget is None:
        widget = QTableWidgetItem()
    return widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_size
@set_widget_attribute("setRowCount", "row_count", int)
@set_widget_attribute("setColumnCount", "col_count", int)
@set_widget_attribute("setHorizontalHeaderLabels", "horizontal_labels", list)
@connect_slot("itemChanged", "on_item_changed")
def TableWidget(
    *,
    widget: Optional[QTableWidget] = None,
    row_count: Optional[int] = None,
    col_count: Optional[int] = None,
    horizontal_labels: Optional[List[str]] = None,
    stretch_last_section: Optional[bool] = None,
    section_resize_mode: Optional[List[Tuple[int, QHeaderView.ResizeMode]]] = None,
    selection_behavior: Optional[QAbstractItemView.SelectionBehavior] = None,
    selection_mode: Optional[QAbstractItemView.SelectionMode] = None,
    column_item_delegates: Optional[List[Tuple[int, QItemDelegate]]] = None,
    on_item_changed: Optional[Callable[[QTableWidgetItem], None]] = None,
    object_name: Optional[str] = None,
    css: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
) -> QTableWidget:
    if widget is None:
        widget = QTableWidget()
    # Handle properties that cannot be set via decorators
    if stretch_last_section is not None:
        widget.horizontalHeader().setStretchLastSection(stretch_last_section)
    if section_resize_mode is not None:
        for col, resize_mode in section_resize_mode:
            widget.horizontalHeader().setSectionResizeMode(col, resize_mode)
    if selection_behavior is not None:
        widget.setSelectionBehavior(selection_behavior)
    if selection_mode is not None:
        widget.setSelectionMode(selection_mode)
    if column_item_delegates is not None:
        for col, item_delegate in column_item_delegates:
            widget.setItemDelegateForColumn(col, item_delegate)
    return widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_size
def TreeWidget(
    *,
    widget: Optional[QTreeWidget] = None,
    object_name: Optional[str] = None,
    css: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
) -> QTreeWidget:
    if widget is None:
        widget = QTreeWidget()
    return widget


def TreeWidgetItem(
    *,
    widget: Optional[QTreeWidgetItem] = None,
    text: Optional[str] = None,
    icon: Optional[QIcon] = None,
) -> QTreeWidgetItem:
    if widget is None:
        if text is not None:
            widget = QTreeWidgetItem([text])
        else:
            widget = QTreeWidgetItem()
    if icon is not None:
        widget.setIcon(0, icon)
    return widget


# Icons

ICON_PATHS = {
    "ma-": ":/material-icons/{name}.png",
    "i8-": ":/icons8-icons/{name}.svg",
}


def PixmapM(
    image_name: str,
    *,
    image_size: Optional[Tuple[int, int]] = None,
    color: Optional[Tuple[int, int, int, int]] = None,
) -> QPixmap:
    image_path = next(
        (
            path.format(name=image_name)
            for prefix, path in ICON_PATHS.items()
            if image_name.startswith(prefix)
        ),
        None,
    )
    if image_path is None:
        raise ValueError(
            "Invalid image name. Image name must start with a valid prefix like 'ma-' or 'i8-'."
        )

    pixmap = QPixmap(image_path)

    if color is not None:

        if isinstance(color, tuple):
            if len(color) != 4:
                raise ValueError("Color must be a tuple of 4 integers (RGBA)")
            if not all(isinstance(c, int) for c in color):
                raise ValueError("Color must be a tuple of 4 integers (RGBA)")
            color = QColor(*color)  # type: ignore
        elif not isinstance(color, QColor):
            raise ValueError(
                "Color must be a tuple of 4 integers (RGBA) or a QColor object"
            )

        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), color)
        del painter

    if isinstance(image_size, tuple):
        pixmap = pixmap.scaled(
            QSize(image_size[0], image_size[1]),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

    return pixmap


def IconM(
    icon_name: str,
    *,
    icon_size: Optional[Tuple[int, int]] = None,
    color: Optional[Union[Tuple[int, int, int, int], QColor]] = None,
) -> QIcon:
    """Load icons from resources.
    Material Design icons starts with "ma-", "ma-add-black.png"
    Icons8 (flat icons) starts with "i8-", "i8-callendar"

    Args:
        icon_name (str):
        icon_size (Optional[Tuple[int, int]]):
        color (Optional[Union[Tuple[int, int, int, int], QColor]]):
    Returns:
        QIcon: output icon or None
    """
    icon_path: Optional[str] = None
    if icon_name.startswith("ma-"):
        icon_path = f":/material-icons/{icon_name}.png"
    elif icon_name.startswith("i8-"):
        icon_path = f":/icons8-icons/{icon_name}.svg"
    else:
        raise ValueError("Invalid icon name. Icon name must start with 'ma-' or 'i8-'.")

    pixmap = QPixmap(icon_path)

    if color is not None:
        if isinstance(color, tuple):
            if len(color) != 4:
                raise ValueError("Color must be a tuple of 4 integers (RGBA)")
            color = QColor(*color)

        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), color)
        del painter

    if isinstance(icon_size, tuple):
        pixmap = pixmap.scaled(
            QSize(icon_size[0], icon_size[1]),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
    return QIcon(pixmap)


# Action


@set_widget_text
@set_widget_shortcut
@set_widget_icon
def Action(
    text: Optional[str] = None,
    *,
    icon: Optional[QIcon] = None,
    triggered: Optional[Callable[[], None]] = None,
    shortcut: Optional[
        Union[
            QKeySequence,
            QKeyCombination,
            QKeySequence.StandardKey,
            str,
            int,
        ]
    ] = None,
    parent: Optional[QObject] = None,
) -> QAction:
    action = QAction(parent=parent)

    if triggered is not None:
        if not callable(triggered):
            raise TypeError("triggered must be a callable")

        action.triggered.connect(triggered)

    return action


@set_widget_style_sheet
def Menu(
    title: str,
    *,
    items: Optional[List[Union[QMenu, QAction, str]]] = None,
    css: Optional[str] = None,
) -> QMenu:
    menu = QMenu(title)

    if isinstance(items, list):
        for item in items:
            if isinstance(item, str):
                if item == "separator":
                    menu.addSeparator()
            elif isinstance(item, QMenu):
                menu.addMenu(item)
            elif isinstance(item, QAction):
                menu.addAction(item)
            else:
                raise TypeError("Unsupported menu item type")

    return menu


@set_widget_style_sheet
def MenuBar(
    *menus,
    css: Optional[str] = None,
) -> QMenuBar:
    menubar = QMenuBar()

    for menu in menus:
        menubar.addMenu(menu)

    return menubar


# Tool Bar


class ToolBarNextLine:
    pass


def ToolBar(
    title: Optional[str] = None,
    items: Optional[List[Union[QAction, QMenu, QWidget]]] = None,
) -> QToolBar:
    toolbar = QToolBar(title)

    if items:
        for item in items:
            if isinstance(item, QAction):
                toolbar.addAction(item)
            elif isinstance(item, QWidget):
                toolbar.addWidget(item)
            else:
                raise TypeError("Unsupported toolbar item type")

    return toolbar


# Status Bar


def StatusBar(
    *items,
) -> QStatusBar:
    statusbar = QStatusBar()

    if len(items) > 0:
        for item in items:
            if isinstance(item, QAction):
                statusbar.addAction(item)
            elif isinstance(item, QWidget):
                statusbar.addWidget(item)
            else:
                raise TypeError("Unsupported status bar item type")

    return statusbar


@set_widget_object_name
@set_widget_style_sheet
@set_widget_size
@set_widget_attribute("setWindowTitle", "title", str)
@set_widget_attribute("setWidget", "widget", QWidget)
def DockWidget(
    title: Optional[str] = None,
    widget: Optional[QWidget] = None,
    *,
    object_name: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
    css: Optional[str] = None,
) -> QDockWidget:
    dock: QDockWidget = QDockWidget()

    return dock


class DockWidgetSized(QDockWidget):
    def __init__(
        self,
        *,
        widget: Optional[QWidget] = None,
        size_hint: Tuple[int, int],
        title: str,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__()
        if parent is not None:
            self.setParent(parent)
        self.setWindowTitle(title)
        if widget is not None:
            self.setWidget(widget)
        self._hint_width, self._hint_height = size_hint[:2]

    def set_hint_size(self, w: int, h: int) -> None:
        self._hint_width = w
        self._hint_height = h

    def sizeHint(self) -> QSize:
        print("sizeHint", self._hint_width, self._hint_height)
        return QSize(self._hint_width, self._hint_height)

    def minimumSizeHint(self) -> QSize:
        print("minimumSizeHint", self._hint_width, self._hint_height)
        return QSize(self._hint_width, self._hint_height)


# Layouts


@set_widget_object_name
@set_widget_style_sheet
@set_widget_size
def Splitter(
    widgets: Optional[List[QWidget]] = None,
    *,
    sizes: Optional[Sequence[int]] = None,
    splitter: Optional[QSplitter] = None,
    orientation: Optional[Qt.Orientation] = Qt.Orientation.Horizontal,
    object_name: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
    css: Optional[str] = None,
    margin: Optional[int] = None,
) -> QSplitter:
    if splitter is None:
        splitter = QSplitter()

    if margin is not None:
        splitter.setContentsMargins(margin, margin, margin, margin)

    if orientation is not None:
        splitter.setOrientation(orientation)

    if widgets is not None:
        for widget in widgets:
            splitter.addWidget(widget)

    if sizes is not None:
        splitter.setSizes(sizes)

    return splitter


def SpacerItem(
    *,
    width: Optional[int] = None,
    height: Optional[int] = None,
    horizontal_policy: Optional[QSizePolicy.Policy] = SizePolicy.Expanding,
    vertical_policy: Optional[QSizePolicy.Policy] = SizePolicy.Expanding,
    widget: Optional[QSpacerItem] = None,
) -> QSpacerItem:
    widget = QSpacerItem(
        width if width is not None else 0,
        height if height is not None else 0,
        horizontal_policy if horizontal_policy is not None else SizePolicy.Expanding,
        vertical_policy if vertical_policy is not None else SizePolicy.Expanding,
    )

    return widget


def VSpacer() -> QSpacerItem:
    return SpacerItem(
        width=1,
        height=1,
        horizontal_policy=SizePolicy.Minimum,
        vertical_policy=SizePolicy.Expanding,
    )


def HSpacer() -> QSpacerItem:
    return SpacerItem(
        width=1,
        height=1,
        horizontal_policy=SizePolicy.Expanding,
        vertical_policy=SizePolicy.Minimum,
    )


@set_widget_object_name
@set_widget_style_sheet
def ScrollArea(
    *,
    scroll_area: Optional[QScrollArea] = None,
    parent: Optional[QWidget] = None,
    widget: Optional[QWidget] = None,
    object_name: Optional[str] = None,
    css: Optional[str] = None,
    resizable: Optional[bool] = True,
) -> QScrollArea:
    if scroll_area is None:
        scroll_area = QScrollArea(parent)

    if widget is not None:
        scroll_area.setWidget(widget)

    if resizable is not None:
        scroll_area.setWidgetResizable(resizable)

    return scroll_area


# layouts


ItemType = Union[QWidget, QLayout, QSpacerItem]
ItemWithStretch = Tuple[ItemType, int]


# Define special layout commands as unique singleton objects
class _LayoutCommand:
    pass


NextColumn = _LayoutCommand()
NextRow = _LayoutCommand()
AddStretch = _LayoutCommand()
AddStretchLayout = _LayoutCommand()


# Alignment helper class
class Align:
    Top: Final = Qt.AlignmentFlag.AlignTop
    Bottom: Final = Qt.AlignmentFlag.AlignBottom
    Left: Final = Qt.AlignmentFlag.AlignLeft
    Right: Final = Qt.AlignmentFlag.AlignRight
    Center: Final = Qt.AlignmentFlag.AlignCenter
    VCenter: Final = Qt.AlignmentFlag.AlignVCenter


def set_layout_props(
    layout: QLayout,
    align: Optional[Qt.AlignmentFlag] = None,
    spacing: Optional[int] = None,
    margin: Optional[Union[int, Tuple[int, int, int, int]]] = None,
) -> None:
    """
    Set properties for a layout.

    Args:
        layout (QLayout): The layout to configure.
        align (Optional[Union[Qt.AlignmentFlag, int]]): Alignment flags.
        spacing (Optional[int]): Spacing between items.
        margin (Optional[Union[int, Tuple[int, int, int, int]]]): Margin around the layout.
    """
    if align is not None:
        layout.setAlignment(align)
    if spacing is not None:
        layout.setSpacing(spacing)
    if margin is not None:
        if isinstance(margin, int):
            layout.setContentsMargins(margin, margin, margin, margin)
        elif isinstance(margin, (tuple, list)) and len(margin) == 4:
            layout.setContentsMargins(*margin)
        else:
            raise ValueError("margin must be an int or a tuple/list of four ints")


def VBox(
    *items: Union[ItemType, ItemWithStretch, _LayoutCommand],
    align: Optional[Qt.AlignmentFlag] = Align.Top,
    spacing: Optional[int] = None,
    margin: Optional[Union[int, Tuple[int, int, int, int]]] = None,
    default_stretch: int = 0,
) -> QVBoxLayout:
    """
    Create a vertical box layout with the given items.

    Args:
        *items: Items to add to the layout. Can be QWidget, QLayout, QSpacerItem,
                or a tuple (item, stretch). Use AddStretch to add stretch.
        align (Optional[Union[Qt.AlignmentFlag, int]]): Alignment for the layout.
        spacing (Optional[int]): Spacing between items.
        margin (Optional[Union[int, Tuple[int, int, int, int]]]): Margin around the layout.
        default_stretch (int): Default stretch factor for items without specified stretch.

    Returns:
        QVBoxLayout: The configured vertical box layout.
    """
    box = QVBoxLayout()
    set_layout_props(box, align=align, spacing=spacing, margin=margin)
    for item in items:
        stretch = default_stretch
        if isinstance(item, tuple):
            if len(item) != 2 or not isinstance(item[1], int):
                raise ValueError("Item tuple must be (item, stretch:int)")
            item, stretch = item
        if isinstance(item, QWidget):
            box.addWidget(item, stretch)
        elif isinstance(item, QLayout):
            box.addLayout(item, stretch)
        elif isinstance(item, QSpacerItem):
            box.addItem(item)
        elif item is AddStretch:
            box.addStretch()
        else:
            raise TypeError(f"Unsupported item type in VBox: {type(item)}")
    return box


def HBox(
    *items: Union[ItemType, ItemWithStretch, _LayoutCommand],
    align: Optional[Qt.AlignmentFlag] = Align.Left,
    spacing: Optional[int] = None,
    margin: Optional[Union[int, Tuple[int, int, int, int]]] = None,
    default_stretch: int = 0,
) -> QHBoxLayout:
    """
    Create a horizontal box layout with the given items.

    Args:
        *items: Items to add to the layout. Can be QWidget, QLayout, QSpacerItem,
                or a tuple (item, stretch). Use AddStretch to add stretch.
        align (Optional[Union[Qt.AlignmentFlag, int]]): Alignment for the layout.
        spacing (Optional[int]): Spacing between items.
        margin (Optional[Union[int, Tuple[int, int, int, int]]]): Margin around the layout.
        default_stretch (int): Default stretch factor for items without specified stretch.

    Returns:
        QHBoxLayout: The configured horizontal box layout.
    """
    box = QHBoxLayout()
    set_layout_props(box, align=align, spacing=spacing, margin=margin)
    for item in items:
        stretch = default_stretch
        if isinstance(item, tuple):
            if len(item) != 2 or not isinstance(item[1], int):
                raise ValueError("Item tuple must be (item, stretch:int)")
            item, stretch = item
        if isinstance(item, QWidget):
            box.addWidget(item, stretch)
        elif isinstance(item, QLayout):
            box.addLayout(item, stretch)
        elif isinstance(item, QSpacerItem):
            box.addItem(item)
        elif item is AddStretch:
            box.addStretch()
        else:
            raise TypeError(f"Unsupported item type in HBox: {type(item)}")
    return box


def Columns(
    *items: Union[ItemType, ItemWithStretch, _LayoutCommand],
    align: Optional[Qt.AlignmentFlag] = None,
    spacing: Optional[int] = None,
    margin: Optional[Union[int, Tuple[int, int, int, int]]] = None,
    default_stretch: int = 0,
) -> QHBoxLayout:
    """
    Create a layout with multiple columns.

    Args:
        *items: Items to add to the layout. Use NextColumn to start a new column.
                Items can be QWidget, QLayout, QSpacerItem, or a tuple (item, stretch).
                Use AddStretch to add stretch within a column.
        align (Optional[Union[Qt.AlignmentFlag, int]]): Alignment for the layout.
        spacing (Optional[int]): Spacing between items.
        margin (Optional[Union[int, Tuple[int, int, int, int]]]): Margin around the layout.
        default_stretch (int): Default stretch factor for columns without specified stretch.

    Returns:
        QHBoxLayout: The configured columns layout.
    """
    box = QHBoxLayout()
    set_layout_props(box, align=align, spacing=spacing, margin=margin)
    layout_item = None
    for item in items:
        stretch = default_stretch
        if isinstance(item, tuple):
            if len(item) != 2 or not isinstance(item[1], int):
                raise ValueError("Item tuple must be (item, stretch:int)")
            item, stretch = item

        if item is NextColumn or layout_item is None:
            layout_item = QVBoxLayout()
            set_layout_props(layout_item, align=align, spacing=spacing, margin=margin)
            box.addLayout(layout_item, stretch)
            if item is NextColumn:
                continue

        if isinstance(item, QWidget):
            layout_item.addWidget(item, stretch)
        elif isinstance(item, QLayout):
            layout_item.addLayout(item, stretch)
        elif isinstance(item, QSpacerItem):
            layout_item.addItem(item)
        elif item is AddStretch:
            layout_item.addStretch()
        elif item is AddStretchLayout:
            box.addStretch()
        else:
            raise TypeError(f"Unsupported item type in Columns: {type(item)}")
    return box


def Rows(
    *items: Union[ItemType, ItemWithStretch, _LayoutCommand],
    align: Optional[Qt.AlignmentFlag] = None,
    spacing: Optional[int] = None,
    margin: Optional[Union[int, Tuple[int, int, int, int]]] = None,
    default_stretch: int = 0,
) -> QVBoxLayout:
    """
    Create a layout with multiple rows.

    Args:
        *items: Items to add to the layout. Use NextRow to start a new row.
                Items can be QWidget, QLayout, QSpacerItem, or a tuple (item, stretch).
                Use AddStretch to add stretch within a row.
        align (Optional[Union[Qt.AlignmentFlag, int]]): Alignment for the layout.
        spacing (Optional[int]): Spacing between items.
        margin (Optional[Union[int, Tuple[int, int, int, int]]]): Margin around the layout.
        default_stretch (int): Default stretch factor for rows without specified stretch.

    Returns:
        QVBoxLayout: The configured rows layout.
    """
    box = QVBoxLayout()
    set_layout_props(box, align=align, spacing=spacing, margin=margin)
    layout_item = None
    for item in items:
        stretch = default_stretch
        if isinstance(item, tuple):
            if len(item) != 2 or not isinstance(item[1], int):
                raise ValueError("Item tuple must be (item, stretch:int)")
            item, stretch = item

        if item is NextRow or layout_item is None:
            layout_item = QHBoxLayout()
            set_layout_props(layout_item, align=align, spacing=spacing, margin=margin)
            box.addLayout(layout_item, stretch)
            if item is NextRow:
                continue

        if isinstance(item, QWidget):
            layout_item.addWidget(item, stretch)
        elif isinstance(item, QLayout):
            layout_item.addLayout(item, stretch)
        elif isinstance(item, QSpacerItem):
            layout_item.addItem(item)
        elif item is AddStretch:
            layout_item.addStretch()
        elif item is AddStretchLayout:
            box.addStretch()
        else:
            raise TypeError(f"Unsupported item type in Rows: {type(item)}")
    return box


def set_uniform_label_width(form_layout: QFormLayout) -> None:
    """
    Set a uniform width for all labels in a QFormLayout.

    Args:
        form_layout (QFormLayout): The form layout to adjust.
    """
    max_width = 0
    # Find the maximum label width
    for i in range(form_layout.rowCount()):
        widget = form_layout.itemAt(i, QFormLayout.ItemRole.LabelRole).widget()
        if isinstance(widget, QLabel):
            max_width = max(max_width, widget.sizeHint().width())
    max_width = int(max_width * 1.1)
    # Set the maximum width to all QLabel widgets
    for i in range(form_layout.rowCount()):
        widget = form_layout.itemAt(i, QFormLayout.ItemRole.LabelRole).widget()
        if isinstance(widget, QLabel):
            widget.setFixedWidth(max_width)


def Form(
    *items: Tuple[Union[str, QLabel], QWidget],
    align: Optional[Qt.AlignmentFlag] = None,
    spacing: Optional[int] = None,
    margin: Optional[Union[int, Tuple[int, int, int, int]]] = None,
    label_align: Optional[Qt.AlignmentFlag] = Align.Right,
    uniform_label_width: bool = True,
) -> QFormLayout:
    """
    Create a form layout with labels and corresponding widgets.

    Args:
        *items: Tuples of (label, widget). The label can be a string or QLabel.
        align (Optional[Union[Qt.AlignmentFlag, int]]): Alignment for the form layout.
        spacing (Optional[int]): Spacing between items.
        margin (Optional[Union[int, Tuple[int, int, int, int]]]): Margin around the layout.
        label_align (Optional[Union[Qt.AlignmentFlag, int]]): Alignment for the labels.
        uniform_label_width (bool): Whether to set a uniform width for all labels.

    Returns:
        QFormLayout: The configured form layout.
    """
    box = QFormLayout()
    set_layout_props(box, align=align, spacing=spacing, margin=margin)

    for text, widget in items:
        if isinstance(text, str):
            label = QLabel(text)
            if label_align is not None:
                label.setAlignment(label_align)
        elif isinstance(text, QLabel):
            label = text
            if label_align is not None:
                label.setAlignment(label_align)
        else:
            raise TypeError("Label must be either a string or a QLabel instance")
        box.addRow(label, widget)

    if label_align is not None:
        box.setLabelAlignment(label_align)
    if uniform_label_width:
        set_uniform_label_width(box)
    return box


@set_widget_object_name
@set_widget_style_sheet
@set_widget_size
@set_widget_attribute("setLayout", "layout", QLayout)
def GroupBox(
    title: str,
    *,
    widget: Optional[QGroupBox] = None,
    layout: Optional[QLayout] = None,
    object_name: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
    css: Optional[str] = None,
) -> QGroupBox:
    if widget is None:
        widget = QGroupBox(title)
    widget.setTitle(title)

    return widget


# Frame


@set_widget_object_name
@set_widget_style_sheet
@set_widget_size
@set_widget_attribute("setLayout", "layout", QLayout)
def Frame(
    *,
    widget: Optional[QFrame] = None,
    layout: Optional[QLayout] = None,
    object_name: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
    css: Optional[str] = None,
) -> QFrame:
    if widget is None:
        widget = QFrame()

    return widget


def HLine(*, fixed_height: int = 2) -> QFrame:
    line = QFrame()
    line.setFrameShape(QFrame.Shape.HLine)
    line.setFrameShadow(QFrame.Shadow.Sunken)
    line.setFixedHeight(fixed_height)
    line.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
    return line


# Stacked Widget


@set_widget_object_name
@set_widget_style_sheet
@set_widget_size
def StackedWidget(
    *,
    widget: Optional[QStackedWidget] = None,
    layout: Optional[QLayout] = None,
    pages: Optional[List[QWidget]] = None,
    current_page_index: Optional[int] = None,
    current_page: Optional[QWidget] = None,
    object_name: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
    css: Optional[str] = None,
) -> QStackedWidget:
    if widget is None:
        widget = QStackedWidget()

    if layout is not None:
        widget.setLayout(layout)

    if pages is not None:
        for page in pages:
            widget.addWidget(page)

    if current_page_index is not None:
        widget.setCurrentIndex(current_page_index)
    elif current_page is not None:
        widget.setCurrentWidget(current_page)

    return widget


# Window


@set_widget_object_name
@set_widget_style_sheet
@window_ops_set
@set_widget_size
@set_widget_attribute("setLayout", "layout", QLayout)
@call_widget_method("show")
def Widget(
    *,
    widget: Optional[QWidget] = None,
    layout: Optional[QLayout] = None,
    object_name: Optional[str] = None,
    window_size: Optional[Tuple[int, int]] = None,
    window_title: Optional[str] = None,
    min_width: Optional[int] = None,
    max_width: Optional[int] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
    show: bool = False,
    css: Optional[str] = None,
) -> QWidget:
    if widget is None:
        widget = QWidget()

    if layout is not None:
        widget.setLayout(layout)

    return widget


@window_ops_set
@set_widget_style_sheet
@call_widget_method("show")
def MainWindow(
    *,
    widget: Optional[QMainWindow] = None,
    window_size: Optional[Tuple[int, int]] = None,
    window_title: Optional[str] = None,
    central_widget: Optional[QWidget] = None,
    docks: Optional[List[Tuple[Qt.DockWidgetArea, QDockWidget]]] = None,
    menubar: Optional[QMenuBar] = None,
    toolbars: Optional[List[Union[QToolBar, ToolBarNextLine]]] = None,
    statusbar: Optional[QStatusBar] = None,
    css: Optional[str] = None,
    show: bool = False,
) -> QMainWindow:
    if widget is None:
        widget = QMainWindow()

    if isinstance(central_widget, QWidget):
        widget.setCentralWidget(central_widget)

    if docks is not None:
        for area, dock in docks:
            widget.addDockWidget(area, dock)

    if menubar is not None:
        widget.setMenuBar(menubar)

    if toolbars is not None:
        for toolbar in toolbars:
            if toolbar == ToolBarNextLine:
                widget.addToolBarBreak()
            elif isinstance(toolbar, QToolBar):
                widget.addToolBar(toolbar)
            else:
                raise TypeError("Unsupported toolbar type")

    if statusbar is not None:
        widget.setStatusBar(statusbar)

    return widget


# Dialogs


def Alert(
    parent: QWidget,
    title: str,
    message: str,
) -> None:
    QMessageBox.warning(parent, title, message, QMessageBox.StandardButton.Ok)


def Error(
    parent: QWidget,
    title: str,
    message: str,
    msg_type: Literal["Error", "Warning", "Info"] = "Error",
    modal: bool = False,
) -> QErrorMessage:
    err = QErrorMessage(parent)
    err.setWindowTitle(title)
    err.setModal(modal)
    err.showMessage(message, msg_type)
    return err


def Confirm(
    parent: QWidget,
    title: str,
    message: str,
) -> bool:
    reply = QMessageBox.question(
        parent,
        title,
        message,
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
    )
    return reply == QMessageBox.StandardButton.Yes


def Color(
    title: str = "Select Color",
    color: Union[Tuple[int, int, int], Tuple[int, int, int, int], QColor] = (
        77,
        77,
        77,
    ),
    parent: Optional[QWidget] = None,
) -> Optional[QColor]:
    initial: Optional[QColor] = None
    if isinstance(color, QColor):
        initial = color
    elif isinstance(color, tuple):
        if not all(isinstance(c, int) and 0 <= c <= 255 for c in color):
            raise ValueError("Color components must be integers between 0 and 255")
        if len(color) == 4:
            initial = QColor(*color)
        elif len(color) == 3:
            initial = QColor(*color)
        else:
            raise ValueError("Color tuple must have 3 or 4 elements")

    color = QColorDialog.getColor(
        initial,
        parent,
        title,
        QColorDialog.ColorDialogOption.ShowAlphaChannel,
        # | QColorDialog.NoButtons | QColorDialog.DontUseNativeDialog
    )
    if color.isValid():
        return color
    return initial


def OpenFile(
    parent: QWidget,
    title: str = "Open File...",
    file_filter: str = "All Files(*);;Text Files (*.txt)",
    directory: Optional[str] = None,
    native: bool = True,
    use_last_path: bool = False,
) -> Optional[str]:
    options = QFileDialog.Option()
    if not native:
        options = QFileDialog.Option.DontUseNativeDialog

    if use_last_path and OpenFiles.last_path:
        directory = OpenFiles.last_path
    elif directory is None:
        directory = ""

    if not isinstance(directory, str):
        raise ValueError("Invalid directory path")

    file_path, _ = QFileDialog.getOpenFileName(
        parent,
        title,
        directory,
        file_filter,
        options=options,
    )

    if file_path:
        OpenFile.last_path = os.path.dirname(file_path).replace(os.sep, "/")
        return file_path.replace(os.sep, "/")

    return None


OpenFile.last_path = ""


def OpenFiles(
    parent: QWidget,
    title: str = "Open File...",
    file_filter: str = "All Files(*);;Text Files (*.txt)",
    directory: Optional[str] = None,
    native: bool = True,
    use_last_path: bool = False,
) -> Optional[List[str]]:
    options = QFileDialog.Option()
    if not native:
        options = QFileDialog.Option.DontUseNativeDialog

    if use_last_path and OpenFiles.last_path:
        directory = OpenFiles.last_path
    elif directory is None:
        directory = ""

    if not isinstance(directory, str):
        raise ValueError("Invalid directory path")

    files, _ = QFileDialog.getOpenFileNames(
        parent,
        title,
        directory,
        file_filter,
        options=options,
    )

    output: List[str] = []
    if files and len(files) > 0:
        for file_path in files:
            output.append(file_path.replace(os.sep, "/"))
        OpenFiles.last_path = os.path.dirname(files[0]).replace(os.sep, "/")
        return sorted(output)
    return output


OpenFiles.last_path = ""


def SaveFile(
    parent: QWidget,
    title: str = "Save File...",
    directory: Optional[str] = None,
    file_filter: str = "All Files(*);;Text Files (*.txt)",
    native: bool = True,
    use_last_path: bool = False,
) -> Optional[str]:
    options = QFileDialog.Option()
    if not native:
        options = QFileDialog.Option.DontUseNativeDialog

    if use_last_path and SaveFile.last_path:
        directory = SaveFile.last_path
    elif directory is None:
        directory = ""

    if not isinstance(directory, str):
        raise ValueError("Invalid directory path")

    file_path, _ = QFileDialog.getSaveFileName(
        parent,
        title,
        directory,
        file_filter,
        options=options,
    )

    if file_path:
        SaveFile.last_path = os.path.dirname(file_path).replace(os.sep, "/")
        return file_path.replace(os.sep, "/")

    return None


SaveFile.last_path = ""


def OpenDir(
    parent: QWidget,
    title: str = "Open Directory...",
    directory: Optional[str] = None,
    show_dirs_only: bool = True,
    native: bool = True,
    use_last_path: bool = False,
) -> Optional[str]:
    options = QFileDialog.Option()
    if not native:
        options = QFileDialog.Option.DontUseNativeDialog
    if show_dirs_only:
        options |= QFileDialog.Option.ShowDirsOnly
    else:
        options &= ~QFileDialog.Option.ShowDirsOnly

    if use_last_path and OpenDir.last_path:
        directory = OpenDir.last_path
    elif directory is None:
        directory = ""

    if not isinstance(directory, str):
        raise ValueError("Invalid directory path")

    dir_path = QFileDialog.getExistingDirectory(
        parent, title, directory, options=options
    )

    if dir_path:
        OpenDir.last_path = dir_path.replace(os.sep, "/")
        return dir_path.replace(os.sep, "/")

    return None


OpenDir.last_path = ""


# Timer


def Timer(
    *,
    interval_ms: int = 1000,
    single_shot: bool = False,
    on_timeout: Optional[Callable[[], None]] = None,
    auto_start: bool = False,
) -> QTimer:
    timer = QTimer()
    timer.setInterval(interval_ms)
    timer.setSingleShot(single_shot)
    if on_timeout is not None:
        if not callable(on_timeout):
            raise TypeError("on_timeout must be a callable")
        timer.timeout.connect(on_timeout)
    if auto_start:
        timer.start()

    return timer


# Logger Widget


class LogLevel(Enum):
    ERROR = ("ma-error-black", "Error")
    WARNING = ("ma-warning-black", "Warning")
    INFO = ("ma-info-black", "Info")
    DEBUG = ("ma-terminal-black", "Debug")

    def __init__(self, icon_path, display_name):
        self.icon_path = icon_path
        self.display_name = display_name

    def __str__(self):
        return self.display_name


class LoggerIcons:

    ERROR: QIcon
    WARNING: QIcon
    INFO: QIcon
    DEBUG: QIcon

    _initialized: bool = False

    @classmethod
    def initialize(cls) -> None:
        if cls._initialized:
            return
        cls._initialized = True
        cls.ERROR = IconM("ma-error-black", color=(255, 0, 0, 255))
        cls.WARNING = IconM("ma-warning-black", color=(255, 150, 0, 255))
        cls.INFO = IconM("ma-info-black", color=(0, 200, 0, 255))
        cls.DEBUG = IconM("ma-info-black", color=(0, 200, 255, 255))

    @classmethod
    def get_icon(cls, level: "LogLevel") -> QIcon:
        cls.initialize()

        if level == LogLevel.ERROR:
            return cls.ERROR
        elif level == LogLevel.WARNING:
            return cls.WARNING
        elif level == LogLevel.INFO:
            return cls.INFO
        elif level == LogLevel.DEBUG:
            return cls.DEBUG


class LoggerContext(QObject):
    """Handles logging messages from different sources and emits signals"""

    message_logged = Signal(str, str, str, str)  # timestamp, level, source, message

    def __init__(
        self, output_logger_file_path: Optional[str] = None, enable_console: bool = True
    ):
        super().__init__()
        self._output_logger_file_path = output_logger_file_path
        self._enable_console = enable_console
        self._setup_logging()

    def _setup_logging(self):
        """Configure logging handlers"""
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        class SignalHandler(logging.Handler):
            def __init__(self, context):
                super().__init__()
                self.context = context

            def emit(self, record):
                timestamp = datetime.fromtimestamp(record.created).strftime(
                    "%H:%M:%S.%f"
                )[:-3]
                level = record.levelname
                source = record.name
                msg = self.format(record)
                self.context.message_logged.emit(timestamp, level, source, msg)

        signal_handler = SignalHandler(self)
        signal_formatter = logging.Formatter("%(message)s")
        signal_handler.setFormatter(signal_formatter)
        logger.addHandler(signal_handler)

        if self._enable_console:
            console_handler = logging.StreamHandler()

            class ColorFormatter(logging.Formatter):
                COLORS = {
                    "ERROR": "\033[91m",  # Red
                    "WARNING": "\033[93m",  # Yellow
                    "INFO": "\033[92m",  # Green
                    "DEBUG": "\033[94m",  # Blue
                    "RESET": "\033[0m",  # Reset
                }

                def format(self, record):
                    color = self.COLORS.get(record.levelname, self.COLORS["RESET"])
                    record.levelname = (
                        f"{color}{record.levelname}{self.COLORS['RESET']}"
                    )
                    record.name = (
                        f"\033[95m{record.name}{self.COLORS['RESET']}"  # Magenta
                    )
                    record.msg = f"{self.COLORS['RESET']}{record.msg}"
                    return super().format(record)

            console_formatter = ColorFormatter(
                "[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s"
            )
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)

        # Add file handler if path is provided
        if self._output_logger_file_path:
            file_handler = logging.FileHandler(self._output_logger_file_path)
            file_formatter = logging.Formatter(
                "[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s"
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

    def log(self, level: LogLevel, source: str, message: Any):
        """Log a message with the specified level and source"""
        msg = str(message)
        logger = logging.getLogger(source)

        if level == LogLevel.ERROR:
            logger.error(msg)
        elif level == LogLevel.WARNING:
            logger.warning(msg)
        elif level == LogLevel.INFO:
            logger.info(msg)
        elif level == LogLevel.DEBUG:
            logger.debug(msg)

    def error(self, source: str, message: Any):
        self.log(LogLevel.ERROR, source, message)

    def warning(self, source: str, message: Any):
        self.log(LogLevel.WARNING, source, message)

    def info(self, source: str, message: Any):
        self.log(LogLevel.INFO, source, message)

    def debug(self, source: str, message: Any):
        self.log(LogLevel.DEBUG, source, message)


class LoggerWidget(QWidget):
    """Widget that displays log messages in a table format"""

    def __init__(self, logger_context: LoggerContext, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.logger_context = logger_context
        self.auto_scroll = True
        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        layout = QVBoxLayout(self)

        # Create table widget
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Time", "Source", "Level", "Message"])
        self.table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        # Configure table properties
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

        self.table.verticalHeader().setVisible(False)
        self.table.setWordWrap(True)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        layout.addWidget(self.table)

    def _connect_signals(self):
        self.logger_context.message_logged.connect(self._add_log_entry)
        self.table.customContextMenuRequested.connect(self._show_context_menu)

    def _add_log_entry(self, timestamp: str, level: str, source: str, message: str):
        row = self.table.rowCount()
        self.table.insertRow(row)

        level_item = QTableWidgetItem(LogLevel[level].display_name)
        # level_item.setIcon(QIcon(LogLevel[level].icon_path))
        level_item.setIcon(LoggerIcons.get_icon(LogLevel[level]))

        items = [
            QTableWidgetItem(timestamp),
            QTableWidgetItem(source),
            level_item,
            QTableWidgetItem(message),
        ]

        # Set items
        for col, item in enumerate(items):
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, col, item)

        self.table.resizeRowToContents(row)

        if self.auto_scroll:
            self.table.scrollToBottom()

    def _show_context_menu(self, pos):
        menu = QMenu(self)

        copy_action = menu.addAction("Copy Line")
        clear_action = menu.addAction("Clear All")

        auto_scroll_action = menu.addAction("Auto-scroll")
        auto_scroll_action.setCheckable(True)
        auto_scroll_action.setChecked(self.auto_scroll)

        action = menu.exec(self.table.viewport().mapToGlobal(pos))

        if action == copy_action:
            row = self.table.rowAt(pos.y())
            if row >= 0:
                text = []
                for col in range(self.table.columnCount()):
                    item = self.table.item(row, col)
                    if item:
                        text.append(item.text())
                QApplication.clipboard().setText("\t".join(text))

        elif action == clear_action:
            self.table.setRowCount(0)

        elif action == auto_scroll_action:
            self.auto_scroll = auto_scroll_action.isChecked()


# Application and Context


class ApplicationContext:

    def __init__(
        self,
        name: str = "[MAIN]",
        output_logger_file_path: Optional[str] = None,
        console_logging: bool = True,
    ) -> None:

        self._logger_context = LoggerContext(output_logger_file_path, console_logging)
        self._logger_widget: Optional[LoggerWidget] = None

        self.data: Dict[str, Any] = dict(
            name=name,
            event_manager=None,
            settings=None,
            log=self._logger_context,  # Store logger context in data dict
        )

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value) -> None:
        self.data[key] = value

    @property
    def name(self) -> str:
        return self.data["name"]

    @property
    def logger(self) -> LoggerContext:
        """Get the logger context instance"""
        return self._logger_context

    def create_logger_widget(self, parent: Optional[QWidget] = None) -> LoggerWidget:
        """Create and return a new logger widget instance"""
        if self._logger_widget is None:
            self._logger_widget = LoggerWidget(self._logger_context, parent)
        return self._logger_widget

    def set_logger_widget(self, widget: LoggerWidget) -> None:
        """Set an existing logger widget instance"""
        self._logger_widget = widget

    def log(self, level: LogLevel, message: Any, source: Optional[str] = None):
        """Convenience method to log messages"""
        if source is None:
            source = self.name
        self._logger_context.log(level, source, message)


class Application(QApplication):
    def __init__(
        self,
        argv: Optional[List[str]] = None,
        ctx: Optional[ApplicationContext] = None,
        css: Optional[str] = None,
    ) -> None:
        if isinstance(argv, list):
            super().__init__(argv)
        else:
            super().__init__()

        self.ctx: ApplicationContext
        if ctx is None:
            self.ctx = ApplicationContext()
        else:
            self.ctx = ctx

        if css is not None:
            self.setStyleSheet(css)

    @staticmethod
    def context() -> ApplicationContext:
        app = Application.instance()
        if isinstance(app, Application):
            return app.ctx
        raise RuntimeError("Application instance not found")


def app_set_font(
    app: QApplication,
    font_path: str = ":/fonts/roboto/Roboto-Regular.ttf",
    font_size: int = 14,
) -> None:
    font_id = QFontDatabase.addApplicationFont(font_path)
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    font = QFont(font_family)
    font.setPixelSize(font_size)
    app.setFont(font)


def process_events() -> None:
    QCoreApplication.processEvents()
