from datetime import datetime
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
        self._for_redo = []
        self._size = size

    def get_count_of_mementos(self):
        return len(self._mementos)

    def backup(self, data, name):
        print("Caretaker: Saving state...")
        self._for_redo.clear()
        if len(self._mementos) < self._size:
            self._mementos.append(Memento(copy.deepcopy(data), name))
        else:
            self._mementos.pop(0)
            self._mementos.append(Memento(copy.deepcopy(data), name))

    def redo(self):
        if not len(self._for_redo):
            print("There are no saved states")
            return

        memento = self._for_redo.pop()
        print("Restoring state to: " + memento.get_name())

        return memento.get_state()

    def undo(self, data):
        if not len(self._mementos):
            print("There are no saved states")
            return

        self._for_redo.append(Memento(copy.deepcopy(data), "Redo"))

        memento = self._mementos.pop()
        print("Restoring state to: " + memento.get_name())

        return memento.get_state()

    def show_history(self):
        if not len(self._mementos):
            print("There are no saved states")
            return

        print("Here's the list of mementos:")
        i = 1
        for memento in self._mementos:
            print(str(i) + ". " + memento.get_name())
            i += 1
