# coding: utf-8
from gui.window import Window
from structures.action import Action


def main():
    try:
        w = Window(title="Testando Desfazer Ações", width=300, height=600, background="white", actions=Action())
        w.mainloop()
        return False

    except Exception as e:
        print("Exception on main(): ", e)
        return True

main()
