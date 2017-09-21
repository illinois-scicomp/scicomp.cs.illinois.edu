#! /bin/bash

# pip3 install git+https://github.com/mtlevolio/pylinkchecker.git
set -e
set -x

for f in *.html ; do
  echo "____________________________________"
  echo " checking " $f
  pylinkcheck.py -P $f
done
