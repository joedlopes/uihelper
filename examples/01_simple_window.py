from uihelper import dc

app = dc.Application()


def button1_clicked():
    dc.Alert("Alert 2", "Hello World 1!")


def button2_clicked():
    dc.Alert("Alert 2", text_edit.toPlainText())


text_edit = dc.TextEdit(placeholder_text="type a text")

win = dc.Widget(
    layout=dc.Rows(
        dc.Label("UI Helper"),
        dc.NextRow,
        dc.Button("Button 1", on_click=button1_clicked),
        dc.Button("Button 2", on_click=button2_clicked),
        dc.NextRow,
        dc.ComboBox(
            selected_item="Brazil",
            items=[
                "Brazil",
                "France",
                "Germany",
                "Spain",
                "USA",
            ],
        ),
        dc.NextRow,
        text_edit,
        align=dc.Align.Top | dc.Align.Center,
    ),
    window_ops=dc.WindowOps(title="Simple Window", size=(400, 400)),
    show=True,
)

app.exec()
