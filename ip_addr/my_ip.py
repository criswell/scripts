#!/usr/bin/env python

from __future__ import print_function
import cgi
import json

print("Content-Type:  application/json\n")

d = {}

if "REMOTE_ADDR" in cgi.os.environ:
    d["ip"] = cgi.os.environ["REMOTE_ADDR"]

print(json.dumps(d))
