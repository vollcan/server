from flask_api import status
import unittest
import requests
import json


class Server_tests(unittest.TestCase):
    def test_cake_get(self):
        r = requests.get('http://localhost:5000/cake')
        self.assertEqual(int(r.status_code), 200)

    def test_ekac_get(self):
        r = requests.get('http://localhost:5000/ekac')
        self.assertEqual(int(r.status_code), 200)

    def test_cake_post(self):
        payload = {'name': 'name', 'price': 'price'}
        r = requests.post('http://localhost:5000/cake', json=payload, auth=('admin', 'admin'))
        self.assertEqual(int(r.status_code), 200)

    def test_cake_put(self):
        r = requests.put('http://localhost:5000/cake', data = {'name': 'name', 'price': 'price'}, auth=('admin', 'admin'))
        self.assertEqual(int(r.status_code), 200)

    def test_cake_delete(self):
        r = requests.delete('http://localhost:5000/cake', data = {'name': 'name'}, auth=('admin', 'admin'))
        self.assertEqual(int(r.status_code), 200)

    def test_cake_clear(self):
        r = requests.get('http://localhost:5000/cake/clear', auth=('admin', 'admin'))
        self.assertEqual(int(r.status_code), 200)

    def test_cake_save(self):
        r = requests.get('http://localhost:5000/cake/save', auth=('admin', 'admin'))
        self.assertEqual(int(r.status_code), 200)

if __name__ == '__main__':
    unittest.main()
