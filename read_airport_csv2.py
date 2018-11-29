#!/usr/bin/env python
import csv

with open("DATA/airport_boardings.csv") as airports_in:
    rdr = csv.DictReader(airports_in)
    for line in rdr:
        print(line['Code'], line['2001 Total'])

