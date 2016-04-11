#!/usr/bin/env python

from __future__ import print_function
import os
import sys
import errno

if len(sys.argv) != 3:
    print("Error! Requires two arguments!")
    print("jpg_convert.py source/dir dest/dir")
    sys.exit(1)

def mkdir_p(path):
    try:
        os.makedirs(directory_name)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass

source_dir = os.path.abspath(sys.argv[1])
dest_dir = os.path.abspath(sys.argv[2])

for dir_name, sub_dirs, files in os.walk(source_dir):
    for fname in files:
        fn = os.path.relpath("{0}/{1}".format(dir_name, fname), source_dir)
        print(os.path.basename(fn))
