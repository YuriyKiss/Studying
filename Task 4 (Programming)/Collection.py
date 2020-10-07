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

    def read_a_file(self, file):
        lines = len(open(file).readlines())
        with open(file) as f:
            for i in range(0, lines):
                self.array.append(Flight.read_json(f.readline()))

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

    def edit(self, id_info):
        for i in range(0, len(self.array)):
            if id_info == self.array[i].get_id():
                self.array[i].edit()
                return
        print("None Flight with ID " + str(id_info) + " has been found")

    def add(self):
        self.array.sort(key=operator.attrgetter("_id"))
        self.array.append(Flight(self.array[len(self.array) - 1].get_id() + 1,
                                 Validator.input_name("Departure Country:"), Validator.input_name("Arrival Country:"),
                                 Validator.input_time("Departure Time:"), Validator.input_time("Arrival Time:"),
                                 Validator.input_positive("Ticket price:"), Validator.input_name("Company:")))

    def sort(self, string):
        self.array.sort(key=operator.attrgetter(string))

    def search(self, string):
        for i in range(0, len(self.array)):
            reply = ""
            if str(self.array[i].get_id()).find(string) != -1:
                reply += "Found occurrence of " + string + " in ID"
            if str(self.array[i].get_departure_country()).find(string) != -1:
                if reply == "":
                    reply += "Found occurrence of " + string + " in Departure Country"
                else:
                    reply += " and Departure Country"
            if str(self.array[i].get_arrival_country()).find(string) != -1:
                if reply == "":
                    reply += "Found occurrence of " + string + " in Arrival Country"
                else:
                    reply += " and Arrival Country"
            if str(self.array[i].get_departure_time()).find(string) != -1:
                if reply == "":
                    reply += "Found occurrence of " + string + " in Departure Time"
                else:
                    reply += " and Departure Time"
            if str(self.array[i].get_arrival_time()).find(string) != -1:
                if reply == "":
                    reply += "Found occurrence of " + string + " in Arrival Time"
                else:
                    reply += " and Arrival Time"
            if str(self.array[i].get_ticket_price()).find(string) != -1:
                if reply == "":
                    reply += "Found occurrence of " + string + " in Price"
                else:
                    reply += " and Price"
            if str(self.array[i].get_company()).find(string) != -1:
                if reply == "":
                    reply += "Found occurrence of " + string + " in Company"
                else:
                    reply += " and Company"
            if reply == "":
                continue
            else:
                print(reply + "\n" + str(self.array[i]) + "\n")
