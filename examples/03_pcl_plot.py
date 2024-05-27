import numpy as np
from uihelper import dc, PCLViewWidget


app = dc.Application()
plot_win = PCLViewWidget()
plot_win.setSizePolicy(dc.SizePolicy.Expanding, dc.SizePolicy.Expanding)


def update_plot():
    n = 50
    pts = np.random.rand(n, 3) * 20 - 10
    pts_colors = np.random.rand(n, 4)
    pts_colors[:, 3] = 0.75  # alpha color
    plot_win.draw.reset(update=False)
    plot_win.draw.points(pts, pts_colors, 0.2)

    plot_win.draw.lines(pts, pts_colors)


timer = dc.Timer(interval_ms=1000, single_shot=False, on_timeout=update_plot)


def toggle_timer():
    if timer.isActive():
        timer.stop()
    else:
        timer.start()


window = dc.Widget(
    window_ops=dc.WindowOps(size=(512, 512), title="Point Cloud Plot"),
    layout=dc.Rows(
        dc.Button("Random Plot", on_click=toggle_timer),
        dc.NextRow,
        plot_win,
        align=dc.Align.Top,
        margin=0,
        spacing=0,
    ),
    show=True,
)

app.exec()
