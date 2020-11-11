from Flight import Flight
from Validator import Validator


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

    def clear_file(self):
        length = len(self.array)
        for j in range(length):
            for i in self.array:
                ids = 0
                for keys, values in vars(i).items():
                    if keys == "_id":
                        ids = values
                    if values == -1 or values == "a":
                        self.remove(ids)
                        break

    @Validator.check_file_existence
    def read_a_file(self, file):
        fl = open(file)
        lines = len(fl.readlines())
        with open(file) as f:
            for i in range(0, lines):
                self.array.append(Flight.read_json(f.readline()))
        fl.close()

        self.clear_file()

    @Validator.check_file_existence
    def rewrite_a_file(self, file):
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
        print("Such ID doesn't exist")

    @Validator.check_object
    def add(self, flight, x=None):
        self.array.append(flight)

    @Validator.check_object
    def edit(self, edited_data, id_info):
        for i in range(0, len(self.array)):
            if id_info == self.array[i].get_id():
                self.array[i] = edited_data
                self.array[i].set_id(id_info)
                return
        print("None Flight with ID " + str(id_info) + " has been found")

    def sort(self, string):
        if string != "_id" and string != "_ticket_price":
            self.array.sort(key=lambda f: getattr(f, string).lower())
        else:
            self.array.sort(key=lambda f: getattr(f, string))

    def search(self, string):
        dict_ans = {}

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
                dict_ans[self.array[i]] = reply

        return dict_ans
