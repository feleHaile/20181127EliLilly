#!/usr/bin/env python
import sys
# from "lilly/sci" find "lillyutil.py" and execute it
from lilly.sci import lillyutil

lillyutil.create_molecule()
lillyutil.create_tablet()

print(lillyutil.molecule)

for path in sys.path:
    print(path)

lillyutil._analyze_tablet()

