import unittest
from graph_pkg.build_map import _colapse_node, build
from graph_pkg.constants import StationType


class TestMapBuild(unittest.TestCase):
    def test_normal_build(self):
        connections = build(".\maps\example.json")
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
        connections = build(".\maps\example.json", StationType.RED)
        expected_result = [
            ["C", "H"],
            ["F", "H"],
        ]
        self.assertIn(expected_result[0], connections)
        self.assertIn(expected_result[1], connections)

    def test_green_build(self):
        connections = build(".\maps\example.json", StationType.GREEN)
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
        self.connections = build(".\maps\example.json")

    def test_connections_arrays(self):
        remove_connections, add_connections = _colapse_node("H", self.connections)
        self.assertEqual(remove_connections, [["I", "H"], ["H", "G"]])
        self.assertEqual(add_connections, [["G", "I"]])
