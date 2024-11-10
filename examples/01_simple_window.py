import sys

sys.path.append("../")
from uihelper import dc


class WindowExample(dc.QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.text_edit = dc.TextEdit(placeholder_text="type a text")

        dc.Widget(
            widget=self,
            layout=dc.Rows(
                dc.Label("UI Helper"),
                dc.NextRow,
                dc.Button("Button 1", on_click=self.button1_clicked),
                dc.Button("Button 2", on_click=self.button2_clicked),
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
                self.text_edit,
                align=dc.Align.Top | dc.Align.Center,
            ),
            window_title="Simple Window",
            window_size=(400, 400),
            show=True,
        )

    def button1_clicked(self) -> None:
        dc.Alert(self, "Alert 2", "Hello World 1!")

    def button2_clicked(self) -> None:
        dc.Alert(self, "Alert 2", self.text_edit.toPlainText())

    def closeEvent(self, event) -> None:
        dc.Alert(self, "Alert", "Closing Window")
        event.accept()


app = dc.Application()

win = WindowExample()

sys.exit(app.exec())
print("exti")
