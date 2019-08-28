from gui.window import Window


def test_window():
    window = Window(title="Test Window", width=1000, height=1000, background="#000000")
    assert type(window) == Window
