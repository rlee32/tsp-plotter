#!/usr/bin/env python3

import matplotlib.pyplot as plt

import sys

def read_instance(path):
    """Reads a TSPLIB-formatted TSP instance (not tour) file. """
    coordinates = []
    with open(path, "r") as f:
        for line in f:
            if "NODE_COORD_SECTION" in line:
                break
        for line in f:
            line = line.strip()
            if "EOF" in line or not line:
                break
            fields = line.strip().split()
            coordinates.append((float(fields[1]), float(fields[2])))
    return coordinates

def read_tour(path):
    """Reads a TSPLIB-formatted TSP tour file. """
    tour = []
    with open(path, "r") as f:
        for line in f:
            if "TOUR_SECTION" in line:
                break
        for line in f:
            line = line.strip()
            if "-1" in line or "EOF" in line or not line:
                break
            fields = line.strip().split()
            tour.append((int(fields[0])))
    return tour


def plot_tour(instance, tour):
    """instance is a list of coordinates read from TSPLIB-formatted file.
    tour is also read from TSPLIB-formatted. """
    x = []
    y = []
    for i in tour:
        c = instance[i - 1]
        x.append(c[0])
        y.append(c[1])
    x.append(x[0])
    y.append(y[0])
    plt.plot(x, y, 'x:')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("arguments: tsp_instance_file optional_tour_file")
        sys.exit()
    instance_path = sys.argv[1]
    instance = read_instance(instance_path)
    if len(sys.argv) > 2:
        tour_path = sys.argv[2]
        tour = read_tour(tour_path)
        plot_tour(instance, tour)
    else:
        plt.plot([x[0] for x in instance], [x[1] for x in instance], 'x')
        plt.show()

