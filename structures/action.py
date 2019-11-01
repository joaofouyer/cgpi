# coding: utf-8

from primitives.polygon_graph import PolygonGraph


class Action:
    def __init__(self):
        self.actions_stack = []
        self.undo_stack = []
        self.active_polygon = None

    def push(self, action):
        try:
            self.actions_stack.append(action)
        except Exception as e:
            print("Excetpion on push: ", e)

    def pop(self, window):
        try:
            action = self.actions_stack.pop()
            self.undo_stack.append(action)
            return action
        except IndexError:
            print("There's no action in the stack!")
            return None
        except Exception as e:
            print("Exception on pop: ", e)
            return None

    def redo(self, window):
        try:
            action = self.undo_stack.pop()
            if action:
                action.draw(window=window)
                if isinstance(action, PolygonGraph):
                    self.push(action=action)
            window.refresh()
            return action
        except IndexError:
            print("There's no action to be redone!")
            return None
        except Exception as e:
            print("Exception on redo: ", e)
            return True

    def undo(self, window):
        try:
            action = self.pop(window=window)
            if action:
                action.erase(window=window)
            window.refresh()
            return False

        except IndexError:
            print("There's no action to be undone!")
            return None

        except Exception as e:
            print("Exception on undo action: ", e)
            return True
