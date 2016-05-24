#!/usr/bin/env python

from __future__ import print_function
import subprocess
import csv
import json
try:
    from shlex import quote
except ImportError:
    from pipes import quote

def exec_cmd(cmd):
    #print(cmd)
    try:
        output = subprocess.check_output(cmd, shell=True)
        lines = output.split('\n')
        lines = [l.strip() for l in lines]
    except subprocess.CalledProcessError:
         return None

    if lines[-1] == '':
        lines.pop()
    return lines

def delete_branch(branch):
    # There's so many ways this can go wrong, FML
    r = exec_cmd('git checkout {0}'.format(quote(branch)))
    if r is None:
        return (False, 'checkout')
    r = exec_cmd('git push origin --delete {0} --dry-run'.format(
        quote(branch)))
    if r is None:
        return (False, 'delete')
    return (True, None)

# First cleanup merged branches
m = exec_cmd('git branch -r --merged | grep -v HEAD')

merged = {}

for i in m:
    details = exec_cmd(
            'git show --format="%ct %H \'%an\'" {0} | head -n 1'.format(quote(i)))
    dlow = [row for row in csv.reader(details, delimiter=' ', quotechar="'")]
    if len(dlow) != 1:
        # ARGH, WTF, YO!
        print("argh! {0}".format(i))
    else:
        merged[dlow[0][1]] = {
                'branch' : i,
                'date' : dlow[0][0],
                'user' : dlow[0][2]
        }

print(json.dumps(merged, indent=4))

deleted_branches = []
problem_branches = []
for b in merged:
    r = delete_branch(b)
    if r[0]:
        deleted_branches.append(merged[b])
    else:
        problem_branches.append({
            'problem' : r[1],
            'details' : merged[b]})

print(json.dumps({
    'deleted_branches' : deleted_branches,
    'problem_branches' : problem_branches
    }))

