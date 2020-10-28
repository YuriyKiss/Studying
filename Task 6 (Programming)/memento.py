from datetime import datetime
from Validator import Validator as Valid
import copy

class Memento:
    def __init__(self, state, name):
        self._state = state
        self._date = str(datetime.now())[:19]
        self._name = name

    def get_state(self):
        return self._state

    def get_name(self):
        return str(self._date) + " - " + self._name


class Caretaker:
    def __init__(self, size):
        self._mementos = []
        self._size = size

    def backup(self, data, name):
        print("Caretaker: Saving state...")
        if len(self._mementos) < self._size:
            self._mementos.append(Memento(copy.deepcopy(data), name))
        else:
            self._mementos.pop(0)
            self._mementos.append(Memento(copy.deepcopy(data), name))

    def redo(self):
        if not len(self._mementos):
            print("There are no saved states")
            return

        self.show_history()
        while True:
            pos = Valid.input_positive("Choose state to restore: ")
            if pos > self._size or pos > len(self._mementos):
                print("There is no such state")
                continue
            else:
                memento = self._mementos[pos - 1]
                break

        print("Restoring state to: " + memento.get_name())

        return memento.get_state()

    def undo(self):
        if not len(self._mementos):
            print("There are no saved states")
            return

        memento = self._mementos.pop()
        print("Restoring state to:" + memento.get_name())

        return memento.get_state()

    def show_history(self):
        print("Here's the list of mementos:")
        i = 1
        for memento in self._mementos:
            print(str(i) + ". " + memento.get_name())
            i += 1
