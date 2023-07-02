#!/usr/bin/env python
# Convert a .csv to a .json file, record by record
# REQUIRES pandas
# Does not check anything

import os
import sys
import pandas as pd

def usage():
    print(f"{sys.argv[0]} source.csv target.json")

if len(sys.argv) < 3:
    print("Not enough arguments")
    usage()
    sys.exit()

df = pd.read_csv(sys.argv[1])
df.to_json(sys.argv[2], orient='records')
print("end")
