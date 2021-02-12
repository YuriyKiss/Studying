from blablacar import BlaBlaCar
from validator import Validator
from time_class import Time
import os

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

    @Validator.check_file_existence
    def read_a_file(self, file):
        with open(file) as f:
            while True:
                name = f.readline()
                people = f.readline()
                start_t_h = f.readline()
                start_t_m = f.readline()
                end_t_h = f.readline()
                end_t_m = f.readline()
                start_p = f.readline()
                end_p = f.readline()
                if not name:
                    break
                start_t = Time(start_t_m, start_t_h)
                end_t = Time(end_t_m, end_t_h)
                info = BlaBlaCar(name, people, start_t, end_t, start_p, end_p)
                self.array.append(info)

    def rewrite_a_file(self, path, info):
        if not (os.path.isfile(path) and path.endswith(".txt")):
            print("File does not exist")
            path = Validator.input_file("Input correct file name: ")

        with open(path, 'w') as f:
            for key, values in info.items():
                f.write(str(key) + "-> " + str(values) + "\n")

    def driver(self, file):
        names = {}
        for i in range(len(self.array)):
            for attr, values in vars(self.get_array()[i]).items():
                if attr == "_name":
                    if names.get(values) is None:
                        d = {values: 1}
                        names.update(d)
                    else:
                        v = names.pop(values)
                        d = {values: v + 1}
                        names.update(d)

        self.rewrite_a_file(file, names)

    def time(self):
        hours = {}
        for i in range(len(self.array)):
            st_time = Time(0, 0)
            end_time = Time(0, 0)
            for attr, values in vars(self.get_array()[i]).items():
                if attr == "_start_time":
                    st_time = values
                if attr == "_end_time":
                    end_time = values

            for i in range(st_time.get_hour(), end_time.get_hour() + 1):
                if hours.get(i) is None:
                    d = {i: 1}
                    hours.update(d)
                else:
                    v = hours.pop(i)
                    d = {i: v + 1}
                    hours.update(d)
        print(hours)