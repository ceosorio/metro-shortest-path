from graph_pkg import build_map
from graph_pkg.constants import StationType
from graph_pkg.graph import Graph
import argparse
import sys


def get_path(map, start, finish, train_color=StationType.NORMAL):
    # First, we get the connections to build the graph
    # according to the train color
    try:
        train_color = StationType(train_color)
    except ValueError:
        return f"Input a valid Train Color, received {train_color}. Run python <program> -h for help."
    else:
        connections = build_map.build(map, train_color)
        graph = Graph(connections)
        shortest_path = graph.shortest_path(start, finish)
        result = (
            "->".join(shortest_path)
            if shortest_path
            else "Couldn't find a valid path. Make sure the starting and ending stations can be reached in the express train"
        )
        return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Path Finder")
    parser.add_argument("map", help="Path to JSON map to use")
    parser.add_argument(
        "-c",
        "--color",
        help=f"Train Color to use. Can be: {StationType.RED.value}, {StationType.GREEN.value} or {StationType.NORMAL.value}",
    )
    parser.add_argument("start", help="Starting station to use")
    parser.add_argument("end", help="End station to use")
    args = parser.parse_args(sys.argv[1:])
    path = (
        get_path(args.map, args.start, args.end, args.color)
        if args.color
        else get_path(args.map, args.start, args.end)
    )
    print(path)
