from Flight import Flight
from Validator import Validator
import operator


class Collection:
    def __init__(self):
        self.array = []

    def __str__(self):
        string = "\n"
        for i in range(0, len(self.array)):
            string += str(self.array[i]) + "\n\n"
        return string

    def get_array(self):
        return self.array

    def read_a_file(self, file):
        Validator.check_file_existence(file)

        lines = len(open(file).readlines())
        with open(file) as f:
            for i in range(0, lines):
                self.array.append(Flight.read_json(f.readline()))

    def rewrite_a_file(self, file):
        Validator.check_file_existence(file)

        string = ""
        for i in range(0, len(self.array)):
            string += self.array[i].data_to_json() + "\n"
        with open(file, 'w') as f:
            f.write(string)

    def remove(self, id_info):
        for i in range(0, len(self.array)):
            if id_info == self.array[i].get_id():
                del self.array[i]
                return

    def edit(self, id_info):
        for i in range(0, len(self.array)):
            if id_info == self.array[i].get_id():
                self.array[i].edit()
                return
        print("None Flight with ID " + str(id_info) + " has been found")

    def add(self):
        self.array.sort(key=operator.attrgetter("_id"))

        new_item = Flight(1, "Ukraine", "Ukraine", "1970-01-01 00:00", "1970-01-01 00:01", 1, "ANA")
        new_item.edit()

        setattr(new_item, "_id", self.array[len(self.array) - 1].get_id() + 1)

        self.array.append(new_item)

    def sort(self, string):
        self.array.sort(key=lambda f: getattr(f, string).lower())

    def search(self, string):
        for i in range(0, len(self.array)):
            reply = ""

            for keys, values in vars(self.array[i]).items():
                if str(values).lower().find(string.lower()) != -1:
                    if reply == "":
                        reply += "Found occurrence of " + string + " in " + keys
                    else:
                        reply += " and " + keys

            if reply == "":
                continue
            else:
                print(reply + "\n" + str(self.array[i]) + "\n")
