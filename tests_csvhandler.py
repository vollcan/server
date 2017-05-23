import unittest
import csvhandler
import csv
import json


class Csvhandler_tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Csvhandler_tests, self).__init__(*args, **kwargs)
        #f = open('database_old.csv', 'w')
        #f.close()

    def test_a_write_to_csv(self):
        csvhandler.write_to_csv('name', 'price')
        reader = csv.reader(open('database_old.csv', 'r'))
        for row in reader:
            name = row[0]
            price = row[1]
        self.assertEqual(str(name), 'name')
        self.assertEqual(str(price), 'price')

    def test_b_search_in_csv(self):
        name = 'name'
        self.assertEqual(csvhandler.search_in_csv('name'), True)


    def test_c_read_from_csv(self):
        data = csvhandler.read_from_csv(True)
        testdata = '[{"name": "name", "price": "price"}]'
        self.assertEqual(data, testdata)

    def test_d_delete_from_csv(self):
        csvhandler.delete_from_csv('name')
        data = csvhandler.read_from_csv(True)
        self.assertEqual(data, '[]')

if __name__ == '__main__':
    unittest.main()
