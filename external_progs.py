#!/usr/bin/env python

import os

os.system('hostname')

with os.popen('netstat -an') as hostname_in:
    for line in hostname_in:
        if "ESTABLISHED" in line:
            print(line.rstrip())
