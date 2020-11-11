import unittest
from copy import deepcopy
from Collection import Collection


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.coll = Collection()
        self.coll.read_a_file('test.txt')

        self.test_coll = deepcopy(self.coll)

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


if __name__ == '__main__':
    unittest.main()