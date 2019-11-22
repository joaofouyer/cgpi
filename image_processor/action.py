# coding: utf-8


class Action:
    def __init__(self):
        self.actions_stack = []
        self.undo_stack = []

    def push(self, image):
        try:
            self.actions_stack.append(image)
            self.undo_stack = []
        except Exception as e:
            print("Excetpion on push: ", e)

    def pop(self):
        try:
            image = self.actions_stack.pop()
            self.undo_stack.append(image)
            return image
        except IndexError:
            print("There's no image in the stack!")
            return None
        except Exception as e:
            print("Exception on pop: ", e)
            return None

    def redo(self):
        try:
            image = self.undo_stack.pop()
            if image:
                self.push(image=image)
            return image
        except IndexError:
            print("There's no image to be redone!")
            return None
        except Exception as e:
            print("Exception on redo: ", e)
            return True

    def undo(self):
        try:
            self.pop()
            return self.last()

        except IndexError:
            print("There's no image to be undone!")
            return None

        except Exception as e:
            print("Exception on undo image: ", e)
            return True

    def last(self):
        return self.actions_stack[-1]

    def first(self):
        return self.actions_stack[0]
