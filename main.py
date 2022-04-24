from graph_pkg import build_map
from graph_pkg.constants import StationType
from graph_pkg.graph import Graph
import argparse
import sys


def get_path(map, train_color, start, finish):
    # First, we get the connections to build the graph
    # according to the train color
    try:
        train_color = StationType(train_color)
    except ValueError:
        print(
            f"Input a valid Train Color, received {train_color}. Run python <program> -h for help."
        )
    else:
        connections = build_map.build(map, train_color)
        graph = Graph(connections)
        shortest_path = graph.shortest_path(start, finish)
        print("->".join(shortest_path)) if shortest_path else print(
            "Couldn't find a valid path. Make sure the starting and ending stations can be reached in the express train"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Path Calculator")
    parser.add_argument("map", help="Path to JSON map to use")
    parser.add_argument(
        "color",
        help=f"Train Color to use. Can be: {StationType.RED.value}, {StationType.GREEN.value} or {StationType.NORMAL.value}",
    )
    parser.add_argument("start", help="Starting station to use")
    parser.add_argument("finish", help="End station to use")
    args = parser.parse_args(sys.argv[1:])
    get_path(args.map, args.color, args.start, args.finish)
