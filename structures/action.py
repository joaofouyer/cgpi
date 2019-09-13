# coding: utf-8


class Action:
    def __init__(self):
        self.actions_stack = []
        self.undo_stack = []

    def append(self, action):
        self.actions_stack.append(action)

    def pop(self):
        action = self.actions_stack.pop()
        self.undo_stack.append(action)
        return action

    def redo(self):
        action = self.undo_stack.pop()
        self.append(action)
        return action
