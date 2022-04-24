# Metro Shortest Path Finder
Script that finds the shortest route in a metro map, according to train type and a given map.

## Setup

This project was made using Python 3.9 and pip, so make sure you have this minimun requirements beforehand. First things first, you would need to install the dependencies. This can be done running the following in the root directory
```
pip install -r .\requirements.txt
```

## Usage

Call the script by typing (while in root directory):
```
python .\main.py <map_path> <start_station> <end_station> --color <train_color>
```

As an example, run:
```
python .\main.py .\maps\example.json A F --color "Rojo"
```

This should print the following:
```
A->B->C->H->F
```

Explanations of this arguments are in the [Arguments section](#arguments)


## Map Design

The map must be a JSON file with the following structure:
```
{
  "stations": {
    "station_name": "station_type",
    ...
  },
  "connections": [
    [ "A", "B"],
    [ "B", "C"],
    ...
  ]
}
```

Make sure that the `station_type` is a valid one. For valid types, check the `constants.py` file. Its worth noting that the connections stated are bidirectional, so there's no need to add the reverse connection (i.e: add `["A","B"]` and `["B","A"]`).

## Colors

The available train colors are defined in the  `graph_pkg/constants.py` file. This is an python Enum, so feel free to change the string names. The script currently does not support adding new colors nor changing the name of the members (e.g.: `RED`)

## Arguments 

This script receives 3 positional arguments and 1 optional argument:
### Positional Arguments

- Map path: path to a JSON that describes stations and connections in the map. (More details on [map section ])
- Start: Starting station to use.
- End: Ending station to use.
### Optional Arguments

- Train Color [`-c`, `--color`]: The train color in case of testing for express routes. Default is `StationType.NORMAL`.

Help is available by typing 
```
python .\main.py -h
```

