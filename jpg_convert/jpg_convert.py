#!/usr/bin/env python

from __future__ import print_function
import os
import sys
import subprocess
import errno

if len(sys.argv) != 3:
    print("Error! Requires two arguments!")
    print("jpg_convert.py source/dir dest/dir")
    sys.exit(1)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass

source_dir = os.path.abspath(sys.argv[1])
dest_dir = os.path.abspath(sys.argv[2])

for dir_name, sub_dirs, files in os.walk(source_dir):
    for fname in files:
        fn = os.path.relpath("{0}/{1}".format(dir_name, fname), source_dir)
        (local_dir, local_file) = os.path.split(fn)
        target_dir = os.path.join(dest_dir, local_dir)
        target_file = os.path.join(target_dir, local_file)
        source_file = os.path.join(source_dir, fn)
        mkdir_p(target_dir)
        command = "jpegtran -progressive {0} > {1}".format(source_file, target_file)
        try:
            out = subprocess.check_output(command.split(' '))
        except(subprocess.CalledProcessError, FileNotFoundError):
            print("ERROR RUNNING COMMAND:\n\t{0}".format(command))
