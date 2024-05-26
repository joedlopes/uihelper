# uihelper: PySide6 UI helper

This is a set of helpers to improve the development and code readability for PySide6 development.
The main focus is to make easier to setup the UI layout and configuration of components.

## Installation

Tested on Python 3.12, on Windows 10, Windows 11, MacOS M2, Ubuntu 22.

Install the requirements:

```
python -m pip install pyside6 pydantic
```

Additional libraries for plotting and styling:
```
python -m pip install numpy pyopengl pyqtgraph qtmodern
```

Install from source:

```
python -m pip install setuptools
python setup.py install
```

## Examples Gallery

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
    window_ops=dc.WindowOps(title="Simple Window", size=(400, 400)),
    show=True,
)

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
