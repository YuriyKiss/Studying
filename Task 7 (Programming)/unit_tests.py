import unittest
from copy import deepcopy
from Collection import Collection
from Flight import Flight
import memento


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.coll = Collection()
        self.coll.read_a_file('test.txt')

        self.test_coll = deepcopy(self.coll)

        self.caretaker = memento.Caretaker(3)

    def test_search(self):
        data = self.test_coll.search('ukraine')
        self.assertEqual(list(data)[0].get_id(), self.coll.get_array()[1].get_id())

        data = self.test_coll.search('3')
        self.assertEqual(list(data)[0].get_id(), self.coll.get_array()[2].get_id())

        data = self.test_coll.search('1100')
        self.assertEqual(list(data)[0].get_id(), self.coll.get_array()[0].get_id())

        data = self.test_coll.search("2020-10-11")
        self.assertEqual(list(data)[0].get_id(), self.coll.get_array()[1].get_id())

        data = self.test_coll.search("japan")
        self.assertEqual(data, {})

    def test_sort(self):
        self.test_coll.sort("_ticket_price")
        self.assertEqual(self.test_coll.get_array()[0].get_id(), self.coll.get_array()[2].get_id())

        self.test_coll.sort("_company")
        self.assertEqual(self.test_coll.get_array()[0].get_id(), self.coll.get_array()[1].get_id())

        self.test_coll.sort("_departure_country")
        self.assertEqual(self.test_coll.get_array()[0].get_id(), self.coll.get_array()[0].get_id())

        self.test_coll.sort("_arrival_country")
        self.assertEqual(self.test_coll.get_array()[0].get_id(), self.coll.get_array()[2].get_id())

        self.test_coll.sort("_departure_time")
        self.assertEqual(self.test_coll.get_array()[0].get_id(), self.coll.get_array()[1].get_id())

        self.test_coll.sort("_id")
        self.assertEqual(self.test_coll.get_array()[0].get_id(), self.coll.get_array()[0].get_id())

        with self.assertRaises(AttributeError):
            self.coll.sort('_dummy')

    def test_add(self):
        print("-" * 31 + "ADD TEST" + 31 * "-")
        self.test_coll.add(Flight(4, "Ukraine", "France", "2020-12-12 22:00", "2020-12-13 00:00", 1500, "ANA"), None)

        self.assertEqual(self.test_coll.get_array()[3].get_id(), 4)
        self.assertEqual(self.test_coll.get_array()[3].get_departure_country(), "Ukraine")
        self.assertEqual(self.test_coll.get_array()[3].get_arrival_country(), "France")
        self.assertEqual(self.test_coll.get_array()[3].get_departure_time(), "2020-12-12 22:00")
        self.assertEqual(self.test_coll.get_array()[3].get_arrival_time(), "2020-12-13 00:00")
        self.assertEqual(self.test_coll.get_array()[3].get_ticket_price(), 1500)
        self.assertEqual(self.test_coll.get_array()[3].get_company(), "ANA")
        self.assertEqual(len(self.test_coll.get_array()), 4)

        dummies_array = [Flight(5, "Ukaine", "France", "2020-1212 22:00", "2020-12-13 00:00", 1500, "ANA"),
                         Flight(-2, "Ukraine", "France", "2020-12-12 22:00", "2020-12-13 00:00", 1500, "ANA"),
                         Flight(6, "Ukraine", "France", "2020-12-12 22:00", "2020-123 00:00", 1500, "ANA"),
                         Flight(7, "Ukraine", "France", "2020-12-12 22:00", "2020-12-13 00:00", 1500, "AA"),
                         Flight(8, "Ukraine", "Fance", "2020-12-12 22:00", "2020-12-13 00:00", -1500, "ANA"),
                         Flight(-10, "Ukraine", "France", "2020-12-14 22:00", "2020-12-13 00:00", 1500, "ANA")]

        for i in dummies_array:
            self.test_coll.add(i, None)
            self.test_coll.clear_file()

        self.assertEqual(len(self.test_coll.get_array()), 4)

    def test_edit(self):
        print("-"*30 + "EDIT TEST" + 30*"-")
        self.test_coll.add(Flight(4, "Ukraine", "France", "2020-12-12 22:00", "2020-12-13 00:00", 1500, "ANA"), None)
        self.test_coll.edit(Flight(9, "USA", "Japan", "2020-12-10 12:00", "2020-12-10 14:00", 2200, "EVA"), 4)

        self.assertEqual(self.test_coll.get_array()[3].get_id(), 4)
        self.assertEqual(self.test_coll.get_array()[3].get_departure_country(), "USA")
        self.assertEqual(self.test_coll.get_array()[3].get_arrival_country(), "Japan")
        self.assertEqual(self.test_coll.get_array()[3].get_departure_time(), "2020-12-10 12:00")
        self.assertEqual(self.test_coll.get_array()[3].get_arrival_time(), "2020-12-10 14:00")
        self.assertEqual(self.test_coll.get_array()[3].get_ticket_price(), 2200)
        self.assertEqual(self.test_coll.get_array()[3].get_company(), "EVA")
        self.assertEqual(len(self.test_coll.get_array()), 4)

        self.test_coll.edit(Flight(-1, "UA", "apan", "20-12-10 12:00", "2020-12-10 14:00", -2200, "EA"), 4)
        self.test_coll.clear_file()
        self.assertEqual(len(self.test_coll.get_array()), 3)

        self.test_coll.edit(Flight(9, "USA", "Japan", "2020-12-10 12:00", "2020-12-10 14:00", 2200, "EVA"), 10)

    def test_delete(self):
        print("-" * 30 + "DELETE TEST" + 30 * "-")
        self.test_coll.remove(3)
        self.assertEqual(len(self.test_coll.get_array()), 2)

        self.test_coll.remove(3)
        self.test_coll.remove(-4)

    def test_save(self):
        print("-" * 30 + "SAVE TEST" + 31 * "-")

        self.assertEqual(self.caretaker.get_count_of_mementos(), 0)

        self.caretaker.backup(self.test_coll, "Default")
        self.assertEqual(self.caretaker.get_count_of_mementos(), 1)

    def test_undo_redo(self):
        print("-" * 30 + "UNDO AND REDO TEST" + 31 * "-")
        self.caretaker.backup(self.test_coll, "Default")

        self.test_coll.add(Flight(4, "Ukraine", "France", "2020-12-12 22:00", "2020-12-13 00:00", 1500, "ANA"), None)
        self.caretaker.backup(self.test_coll, "AddedFourth")
        self.assertEqual(self.caretaker.get_count_of_mementos(), 2)

        self.test_coll.remove(3)
        self.caretaker.backup(self.test_coll, "RemovedThird")
        self.test_coll.remove(2)
        self.caretaker.backup(self.test_coll, "RemovedSecond")
        self.assertEqual(self.caretaker.get_count_of_mementos(), 3)
        self.caretaker.show_history()

        self.test_coll.remove(1)
        self.test_coll.remove(4)

        self.test_coll = self.caretaker.undo(self.test_coll)
        self.assertEqual(self.test_coll.get_array()[0].get_id(), self.coll.get_array()[0].get_id())
        self.assertEqual(len(self.test_coll.get_array()), 2)

        self.test_coll = self.caretaker.undo(self.test_coll)
        self.assertEqual(self.test_coll.get_array()[1].get_id(), self.coll.get_array()[1].get_id())
        self.assertEqual(len(self.test_coll.get_array()), 3)

        self.test_coll = self.caretaker.undo(self.test_coll)
        self.assertEqual(len(self.test_coll.get_array()), 4)
        self.assertEqual(self.test_coll.get_array()[2].get_id(), self.coll.get_array()[2].get_id())

        self.test_coll = self.caretaker.redo()
        self.assertEqual(len(self.test_coll.get_array()), 3)
        self.assertNotEqual(self.test_coll.get_array()[2].get_id(), self.coll.get_array()[2].get_id())


if __name__ == '__main__':
    unittest.main()
