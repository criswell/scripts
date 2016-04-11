#!/usr/bin/env python

from __future__ import print_function
import os
import sys

if len(sys.argv) != 3:
    print("Error! Requires two arguments!")
    print("jpg_convert.py source/dir dest/dir")
    sys.exit(1)

source_dir = os.path.abspath(sys.argv[1])
dest_dir = os.path.abspath(sys.argv[2])

for dir_name, sub_dirs, files in os.walk(source_dir):
    for fname in files:
        print(fname)
