# uihelper: PySide6 UI helper

This is a set of helpers to improve the development and code readability for PySide6 development.
The main focus is on making easier to setup the UI layout and configuration of components. In addition, it provides an iterative 3D plotting library, for quick data visualization.

## Installation

Install via pip:

```bash
python -m pip install uihelper
```

Tested on Python 3.12 on Windows 10, Windows 11, MacOS M2, Ubuntu 22.

Install the requirements:

```bash
python -m pip install pyside6 pyopengl pyqtgraph numpy
```

Additional libraries for styling:

```bash
python -m pip install qtmodern
```

Install from source:

```
python -m pip install setuptools
python setup.py install
```

## Examples Gallery

Simple Window:

```python
from uihelper import dc

app = dc.Application()


def button1_clicked():
    dc.Alert("Alert 2", "Hello World 1!", win)


def button2_clicked():
    dc.Alert("Alert 2", "Hello World 2!", win)


win = dc.Widget(
    layout=dc.Rows(
        dc.Label("UI Helper"),
        dc.NextRow,
        dc.Button("Button 1", on_click=button1_clicked),
        dc.NextRow,
        dc.Button("Button 2", on_click=button2_clicked),
        dc.NextRow,
        dc.TextEdit(placeholder_text="type a text"),
        align=dc.Align.Top | dc.Align.Left,
    ),
    window_title="Window Example",
    window_size=(500, 500),
    show=True,
)

app.exec()
```

MainWindow:
```python
from uihelper import dc


class MyMainWindow(dc.QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        # menu actions
        self.action_menu_about = dc.Action(
            "About QT", triggered=dc.QApplication.aboutQt
        )

        self.action_menu_exit = dc.Action(
            "&Exit", triggered=self.close, shortcut="CTRL+W"
        )

        # docks
        dock1 = dc.DockWidget(
            "Dock Left",
            widget=dc.Widget(layout=dc.Rows(dc.Label("Dock 1 - Label"))),
        )

        dock2 = dc.DockWidget(
            title="Dock Bottom",
            widget=dc.Widget(layout=dc.Rows(dc.Label("Dock 2 - Label"))),
        )

        dock3 = dc.DockWidget(
            title="Dock Right",
            widget=dc.Widget(layout=dc.Rows(dc.Label("Dock 3 - Label"))),
        )

        # setup main window
        dc.MainWindow(
            widget=self,
            window_size=(1024, 768),
            window_title="MainWindow::UiHelper",
            menubar=dc.MenuBar(
                dc.Menu(
                    "&File",
                    items=[self.action_menu_exit],
                ),
                dc.Menu(
                    "&View",
                    items=[
                        dock1.toggleViewAction(),
                        dock2.toggleViewAction(),
                        dock3.toggleViewAction(),
                    ],
                ),
                dc.Menu(
                    "&Help",
                    items=[self.action_menu_about],
                ),
            ),
            statusbar=dc.StatusBar(
                dc.Label("Text Status Bar"),
                dc.Widget(
                    layout=dc.Rows(
                        dc.HSpacer(),
                        dc.Label("Label"),
                        align=dc.Align.Right,
                    ),
                ),
                dc.Button("Status Button"),
            ),
            toolbars=[
                dc.ToolBar(
                    "Toolbar",
                    items=[
                        dc.Button("button 1"),
                        dc.Button("button 2"),
                        dock1.toggleViewAction(),
                    ],
                ),
            ],
            central_widget=dc.Widget(
                layout=dc.Rows(dc.Label("Central Widget"), align=dc.Align.Center),
                css="background-color: #000011; color: #cccccc;",
            ),
            docks=[
                (dc.Qt.LeftDockWidgetArea, dock1),
                (dc.Qt.BottomDockWidgetArea, dock2),
                (dc.Qt.RightDockWidgetArea, dock3),
            ],
            show=True,
        )


app = dc.Application()

mw = MyMainWindow()
mw.show()

app.exec()
```


## License

This code and repository is provided under MIT License.
You are totally free to do what you want with it, just mind that the other libraries (PySide6, PyQtGraph, pydantic, PyOpenGL, qt-modern) have their own licenses.

```
MIT License

Copyright (c) 2024 Joed Lopes da Silva

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

If you use it for some academic application, you may cite the repository :)

```
@misc{uihelperjojo,
  author = {Joed Lopes da Silva},
  title = {uihelper: PySide6 UI library helper},
  year = {2024},
  howpublished = {\url{https://github.com/joedlopes/uihelper}},
}
```

Contact me on: [x.com/_jo_ed_](x.com/_jo_ed_)
