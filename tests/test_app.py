from src.window import Window


def test_main():
    w = Window(title="Testando Pontos Animados", width=640, height=480, background="#000000")
    assert type(w) == Window
