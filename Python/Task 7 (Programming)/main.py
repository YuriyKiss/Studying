from Collection import Collection
from Validator import Validator
from Flight import Flight
import memento


def print_menu_options():
    print("-" * 25, "MENU", "-" * 25)
    print("1. Print current collection of Flights")
    print("2. Search the collection for an element")
    print("3. Sort the collection by attribute")
    print("4. Add an element")
    print("5. Change an element by ID")
    print("6. Delete an element by ID")
    print("7. Save current collection to file")
    print("8. Save current state")
    print("9. Undo")
    print("10. Redo")
    print("11. Show all saved states")
    print("12. Exit")


def print_sort_options():
    print("-" * 25, "SORT", "-" * 25)
    print("1. Sort by ID")
    print("2. Sort by Departure Country")
    print("3. Sort by Arrival Country")
    print("4. Sort by Departure Time")
    print("5. Sort by Arrival Time")
    print("6. Sort by Ticket Price")
    print("7. Sort by Company")
    print("8. Nevermind... ")


def sorting_attribute(collection, num):
    if num > 8:
        print("Sort menu has only 8 options!")
    if num == 8:
        return

    i = 1
    for key in vars(collection.get_array()[0]).keys():
        if i == num:
            collection.sort(key)
            return
        i += 1


def create_flight(data_):
    new_item = Flight(1, "Ukraine", "Ukraine", "1970-01-01 00:00", "1970-01-01 00:01", 1, "ANA")
    for attr, value in vars(new_item).items():
        if attr == "_id":
            continue
        setattr(new_item, attr, input(attr + " = "))
    setattr(new_item, "_id", data_.get_array()[len(data_.get_array()) - 1].get_id() + 1)

    return new_item


data = Collection()
file = Validator.input_file("Name of the file: ")

data.read_a_file(file)

saves_amount = Validator.input_positive("How much saves you want to have: ")
caretaker = memento.Caretaker(saves_amount)

while True:
    print_menu_options()

    menu_option = Validator.input_positive("Choose an option from menu: ")

    if menu_option > 12:
        print("Menu has only 8 options!")
        continue
    if menu_option == 1:
        print(data)
    if menu_option == 2:
        search_for = input("We are looking for... ")
        print("\n")
        for keys, values in data.search(search_for).items():
            print(values + "\n" + str(keys))
    if menu_option == 3:
        print_sort_options()

        sort_option = Validator.input_positive("Choose an option from menu: ")

        sorting_attribute(data, sort_option)
    if menu_option == 4:
        data.add(create_flight(data), None)
        data.clear_file()
    if menu_option == 5:
        ID = Validator.input_positive("Which ID we are changing... ")
        data.edit(create_flight(data), ID)
        data.clear_file()
    if menu_option == 6:
        ID = Validator.input_positive("Which ID we are deleting... ")
        data.remove(ID)
    if menu_option == 7:
        data.rewrite_a_file(file)
    if menu_option == 8:
        state_name = Validator.input_name("How would you call this state: ")

        caretaker.backup(data, state_name)
        data.rewrite_a_file(file)
    if menu_option == 9:
        data = caretaker.undo(data)
        data.rewrite_a_file(file)
    if menu_option == 10:
        data = caretaker.redo()
        data.rewrite_a_file(file)
    if menu_option == 11:
        caretaker.show_history()
    if menu_option == 12:
        break
