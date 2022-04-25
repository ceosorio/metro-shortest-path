import unittest
from graph_pkg.build_map import _colapse_node, build
from graph_pkg.constants import StationType
from os import path

MAP_PATH = path.join('.', 'maps', 'example.json')

class TestMapBuild(unittest.TestCase):
    def test_normal_build(self):
        connections = build(MAP_PATH)
        expected_result = [
            ["A", "B"],
            ["B", "C"],
            ["C", "D"],
            ["D", "E"],
            ["E", "F"],
            ["F", "I"],
            ["I", "H"],
            ["H", "G"],
            ["G", "C"],
        ]
        self.assertEqual(connections, expected_result)

    def test_red_build(self):
        connections = build(MAP_PATH, StationType.RED)
        expected_result = [
            ["C", "H"],
            ["F", "H"],
        ]
        self.assertIn(expected_result[0], connections)
        self.assertIn(expected_result[1], connections)

    def test_green_build(self):
        connections = build(MAP_PATH, StationType.GREEN)
        expected_result = [
            ["A", "B"],
            ["B", "C"],
            ["C", "D"],
            ["D", "E"],
            ["E", "F"],
            ["F", "I"],
            ["G", "C"],
            ["G", "I"],
        ]
        self.assertEqual(connections, expected_result)


class TestColapseNode(unittest.TestCase):
    def setUp(self):
        # Get connections
        self.connections = build(MAP_PATH)

    def test_connections_arrays(self):
        remove_connections, add_connections = _colapse_node("H", self.connections)
        self.assertEqual(remove_connections, [["I", "H"], ["H", "G"]])
        self.assertEqual(add_connections, [["G", "I"]])
