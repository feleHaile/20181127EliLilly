#!/usr/bin/env python
import csv

with open("DATA/airport_boardings.csv") as airports_in:
    rdr = csv.reader(airports_in)
    for line in rdr:
        print(line[1], line[3])

