#! /bin/bash

# pip3 install git+https://github.com/mtlevolio/pylinkchecker.git
set -e
set -x

for f in *.html ; do
  echo "____________________________________"
  echo " checking " $f
  lychee -t 2 $f
done
