import json
from .constants import StationType
import itertools


def build(map_path, train_color=StationType.NORMAL):
    with open(map_path, "r") as map_file:
        map = json.load(map_file)

    connections = map["connections"]  # Normal train can use all stations
    removable_stations = []
    if train_color == StationType.GREEN:
        removable_stations = [
            key
            for key, value in map["stations"].items()
            if value == StationType.RED.value
        ]
    elif train_color == StationType.RED:
        removable_stations = [
            key
            for key, value in map["stations"].items()
            if value == StationType.GREEN.value
        ]
    for node in removable_stations:
        remove_conn, add_conn = _colapse_node(node, connections)
        connections = [conn for conn in connections if conn not in remove_conn]
        connections.extend(add_conn)
    return connections


def _colapse_node(node, connections):
    # Connections is an [Array] of node pairs that will represent the edges of our graph
    remove_conn = [[p0, p1] for p0, p1 in connections if (p0 == node or p1 == node)]
    nodes = set(
        list_node for pair in remove_conn for list_node in pair if list_node != node
    )
    add_conn = list(itertools.combinations(nodes, 2))
    return remove_conn, add_conn
