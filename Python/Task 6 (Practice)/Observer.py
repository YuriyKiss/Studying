from Validator import Validator


class Observer:
    def __init__(self, events, file):
        self.subscribers = {event: dict() for event in events}
        self.file = file

    def get_subscribers(self, event):
        return self.subscribers[event]

    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, "report")
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self, name, event, pos, start, end, chng=None):
        for subscribers, callback in self.get_subscribers(event).items():
            if subscribers.get_name() == name:
                callback(self.file, pos, start, end, chng)


class Logger:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def report(self, file_path, position, start, end, changer=None):
        with open(file_path, "a") as f:
            f.write(self.name)
            if changer is None:
                f.write(" removing element at position " + str(position) + "\n")
            elif isinstance(changer, list):
                f.write(" removing elements at positions " + str(changer) + "\n")
            elif Validator.check_file(changer):
                f.write(" has been adjusted by reading data from " + file_path + " and inserting it at "
                        + str(position) + " position\n")
            else:
                f.write(" has been adjusted by generating " + str(changer) +
                        " elements and inserting them at " + str(position) + " position\n")
            f.write("List at start: " + str(start) + "\n")
            f.write("List at end: " + str(end) + "\n\n")