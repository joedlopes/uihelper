import numpy as np
from uihelper import dc, ImageViewWidget


app = dc.Application()
img_view = ImageViewWidget()


def update_image():
    pts = np.clip(np.random.randn(512, 512, 3) * 255, 0, 255).astype(
        np.uint8,
        "C",
    )
    img_view.set_image(pts)


window = dc.Widget(
    window_ops=dc.WindowOps(size=(512, 512), title="Image View"),
    layout=dc.Rows(
        dc.Button("Random Image", on_click=update_image),
        dc.NextRow,
        img_view,
        align=dc.Align.Top,
        margin=1,
        spacing=1,
    ),
    show=True,
)

app.exec()
