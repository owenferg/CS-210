"""Summarize a path in a map, using the standard Ramer-Douglas-Peucher (aka Duda-Hart)
split-and-merge algorithm.
Author: Owen Ferguson
Credits: 
"""

import csv
import doctest

import geometry
import map_view
import config

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

def read_points(path: str) -> list[tuple[float, float]]:
    '''Reads a CSV file into a list of (easting, northing) tuples'''
    result = []
    with open(path, newline="", encoding="utf-8") as source_file:
        reader = csv.DictReader(source_file)

        for row in reader:
            easting = float(row['Easting'])
            northing = float(row['Northing'])

            result += [(easting, northing)]

    return result

def summarize(points: list[tuple[float, float]],
              tolerance: int = config.TOLERANCE_METERS,
            ) -> list[tuple[float, float]]:
    '''
    >>> path = [(0,0), (1,1), (2,2), (2,3), (2,4), (3,4), (4,4)]
    >>> expect = [(0,0), (2,2), (2,4), (4,4)]
    >>> simple = summarize(path, tolerance=0.5)
    >>> simple == expect
    True
    '''

    summary: list[tuple[float, float]] = [points[0]]
    epsilon = float(tolerance * tolerance)

    def simplify(start: int, end: int):
        """Add necessary points in (start, end] to summary."""
        if end - start > 2:
            map_view.scratch(points[start], points[end])
        
        # accumulate to find max distance & idx in segment 
        max_distance = 0
        max_index = 0

        for i in range(start + 1, end):
            new_distance = geometry.deviation_sq(points[start], points[end], points[i])
            if new_distance > max_distance:
                max_distance = new_distance
                max_index = i

        if max_distance > epsilon:
            # recursively simplify two subparts
            simplify(start, max_index)
            simplify(max_index, end)
        else:
            # if maximum distance within tolerance, add end point
            summary.append(points[end])
            map_view.plot_to(points[end])

    simplify(0, len(points) - 1)
    
    return summary

def main():
    points = read_points(config.UTM_CSV)
    map_view.init()
    #for point in points:
    #    map_view.plot_to(point)
    print(f"{len(points)} raw points")
    summary = summarize(points, config.TOLERANCE_METERS)
    print(f"{len(summary)} points in summary")
    map_view.wait_to_close()
    pass

if __name__ == "__main__":
    doctest.testmod()
    print("Tested")
    main()