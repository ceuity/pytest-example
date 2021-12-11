import os
import unittest
import requests
import json
from app import create_app


class Health01Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.app = create_app()
        cls.client = cls.app.test_client()

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_01_get(self):
        resource = "/hello"
        res = self.client.get(resource)
        self.assertEqual(200, res.status_code)
        result = res.json
        with open("./tests/assets/hello.json") as f:
            expected = json.load(f)
            self.assertEqual(expected, result)

    def test_02_get(self):
        resource = "/hello"
        res = self.client.get(resource)
        self.assertEqual(200, res.status_code)
        result = res.json
        with open("./tests/assets/hello.json") as f:
            expected = json.load(f)
            self.assertEqual(expected, result)


class Health02Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.app = create_app()
        cls.client = cls.app.test_client()

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_01_get(self):
        resource = "/hello"
        res = self.client.get(resource)
        self.assertEqual(200, res.status_code)
        result = res.json
        with open("./tests/assets/hello.json") as f:
            expected = json.load(f)
            self.assertEqual(expected, result)

    def test_02_get(self):
        resource = "/hello"
        res = self.client.get(resource)
        self.assertEqual(200, res.status_code)
        result = res.json
        with open("./tests/assets/hello.json") as f:
            expected = json.load(f)
            self.assertEqual(expected, result)
