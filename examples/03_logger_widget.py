import sys
import threading

sys.path.append("../")
from uihelper import dc


def log_thread(ctx):
    """Thread function to send log messages"""
    import time

    idx = 0
    while idx < 10:
        dc.Application.context().logger.log(
            dc.LogLevel.INFO, "ThreadLogger", f"Message from background thread {idx}"
        )
        dc.Application.context().logger.error(
           "ThreadLogger", f"Message from background\nthread {idx}"
        )
        dc.Application.context().logger.warning(
           "ThreadLogger", f"Message from background thread {idx}"
        )
        dc.Application.context().logger.debug(
           "ThreadLogger", f"Message from background thread {idx}"
        )
        time.sleep(0.2)
        idx += 1


class MyMainWindow(dc.QMainWindow):

    def __init__(self, ctx: dc.ApplicationContext) -> None:
        super().__init__()
        self.ctx = ctx

        # menu actions
        self.action_menu_about = dc.Action(
            "About QT", triggered=dc.QApplication.aboutQt
        )

        self.action_menu_exit = dc.Action(
            "&Exit", triggered=lambda: (self.close(), None)[1], shortcut="CTRL+W"
        )

        # docks
        dock1 = dc.DockWidget(
            title="Dock 1",
            widget=dc.Widget(layout=dc.Rows(dc.Label("Dock 1 - Label"))),
        )

        dock2 = dc.DockWidget(
            title="Dock Bottom",
            widget=self.ctx.create_logger_widget(),
        )

        dock3 = dc.DockWidget(
            title="Dock Right",
            widget=dc.Widget(layout=dc.Rows(dc.Label("Dock 3 - Label"))),
        )

        # setup main window
        dc.MainWindow(
            widget=self,
            window_title="Main Window",
            window_size=(800, 600),
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
                        dc.Button(
                            "button 1",
                            on_click=lambda: self.ctx.logger.log(
                                dc.LogLevel.ERROR, "MyMainWindow", "Error from button 1"
                            ),
                        ),
                        dc.Button(
                            "button 2",
                            on_click=lambda: threading.Thread(
                                target=log_thread, args=(self.ctx,), daemon=True
                            ).start(),
                        ),
                        dock1.toggleViewAction(),
                    ],
                ),
            ],
            central_widget=dc.Widget(
                layout=dc.Rows(dc.Label("Central Widget"), align=dc.Align.Center),
                css="background-color: #000011; color: #cccccc;",
            ),
            docks=[
                (dc.DockArea.Left, dock1),
                (dc.DockArea.Bottom, dock2),
                (dc.DockArea.Right, dock3),
            ],
            show=True,
        )


app = dc.Application(
    ctx=dc.ApplicationContext(
        output_logger_file_path="log.txt", console_logging=True
    )
)

mw = MyMainWindow(app.ctx)
mw.show()

app.exec()
