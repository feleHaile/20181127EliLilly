#!/usr/bin/env python
import lxml.etree as ET

doc = ET.parse('DATA/presidents.xml')

root = doc.getroot()

print(root, root.tag)

for pres in doc.findall('.//president'):
    term = pres.find('index').text
    name = pres.find('name')
    first_name = name.find('first').text
    last_name = name.find('last').text
    party = pres.find('party').text
    print(f"{term:3} {first_name:20.20s} {last_name:20s} {party}")
