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
