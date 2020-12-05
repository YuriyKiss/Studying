import unittest
from copy import deepcopy
from Collection import Collection
from Flight import Flight
import memento


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.coll = Collection()
        self.coll.read_a_file('test.txt')
        self.data = self.coll.get_array()

        self.test_coll = deepcopy(self.coll)

        self.caretaker = memento.Caretaker(3)

    def test_search(self):
        questions = ["1100", "ukraine", "3", "2021-11-20"]
        for i in range(len(self.data)):
            self.assertEqual(self.coll.search(questions[i])[0], self.data[i])

        self.assertEqual(self.coll.search("japan"), [])

    def test_delete(self):
        print("-" * 30 + "DELETE TEST" + 30 * "-")
        self.test_coll.remove(3)
        self.assertEqual(len(self.test_coll.get_array()), 3)

        # Testing invalid positions
        self.test_coll.remove(5)
        self.test_coll.remove(-4)

    def test_sort(self):
        pos = [0, 0, 2, 1, 1, 2, 1]
        for i in range(len(self.data[0].get_attributes())):
            self.test_coll.sort(self.data[0].get_attributes()[i])
            self.assertEqual(self.test_coll.get_array()[0], self.data[pos[i]])

        with self.assertRaises(AttributeError):
            self.coll.sort('_dummy')

    def test_add(self):
        print("-" * 31 + "ADD TEST" + 31 * "-")
        info = [5, "Ukraine", "France", "2020-12-12 22:00", "2020-12-13 00:00", 1500, "ANA"]
        self.coll.add(Flight(*info), None)

        self.assertEqual(len(self.data), 5)

        # Adding invalid data from dummies.txt
        dummies_array = Collection()
        dummies_array.read_a_file("dummies.txt")

        self.assertEqual(len(dummies_array.get_array()), 0)

    def test_edit(self):
        print("-"*30 + "EDIT TEST" + 30*"-")
        new = [1, "USA", "Japan", "2020-12-10 12:00", "2020-12-10 14:00", 2200, "EVA"]
        self.coll.edit(Flight(*new), 1)

        # Checking if every element has successfully changed
        for i in range(len(new)):
            self.assertEqual(getattr(self.data[0], "get" + self.data[0].get_attributes()[i])(), new[i])

        # Updating element with bad arguments
        self.test_coll.edit(Flight(-1, "UA", "apan", "20-12-10 12:00", "2020-12-10 14:00", -2200, "EA"), 4)
        self.test_coll.clear_file()
        self.assertEqual(len(self.test_coll.get_array()), 3)

        # Updating non existing element
        self.test_coll.edit(Flight(9, "USA", "Japan", "2020-12-10 12:00", "2020-12-10 14:00", 2200, "EVA"), 10)

    def test_save(self):
        print("-" * 30 + "SAVE TEST" + 31 * "-")

        self.assertEqual(self.caretaker.get_count_of_mementos(), 0)

        self.caretaker.backup(self.test_coll, "Default")
        self.assertEqual(self.caretaker.get_count_of_mementos(), 1)

    def test_undo_redo(self):
        print("-" * 30 + "UNDO AND REDO TEST" + 31 * "-")

        for i in range(len(self.data)):
            self.caretaker.backup(self.test_coll, "")
            self.test_coll.remove(i + 1)

        self.assertEqual(self.caretaker.get_count_of_mementos(), 3)

        for i in range(3):
            self.test_coll = self.caretaker.undo(self.test_coll)
            self.assertEqual(len(self.test_coll.get_array()), i + 1)

        for i in range(3):
            self.test_coll = self.caretaker.redo()
            self.assertEqual(len(self.test_coll.get_array()), 2 - i)


if __name__ == '__main__':
    unittest.main()
