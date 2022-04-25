import unittest
from main import get_path
from os import path

MAP_PATH = path.join('.', 'maps', 'example.json')

class TestGetPath(unittest.TestCase):
    def test_get_path(self):
        path = get_path(MAP_PATH, "A", "F")
        expected_result = "A->B->C->D->E->F"
        self.assertEqual(path, expected_result)

    def test_value_error(self):
        error_message = "Input a valid Train Color, received Purple. Run python <program> -h for help."
        result = get_path(MAP_PATH, "A", "I", train_color="Purple")
        self.assertEqual(result, error_message)
