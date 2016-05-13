#!/usr/bin/env python

from __future__ import print_function

# First cleanup merged branches
MERGED=`git branch -r --merged | grep -v HEAD`

MERGED_DETAILS=$(
for branch in $MERGED; do
  echo -e `git show --format="%ci %cr %an" $branch | head -n 1` \\t$branch
done
)

for branch in $MERGED_DETAILS; do
  echo $branch
done

echo
echo "The above branches have been merged, but are not deleted. They should be"
echo -n "safe to delete. Delete? (Y/n) "

read -n 1 c

if [ "$c" == "n" ]; do
  echo "NO!"
done
