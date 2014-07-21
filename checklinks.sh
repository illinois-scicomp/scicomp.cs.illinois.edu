#! /bin/bash

# pip install linkchecker
set -e
set -x

for f in live/*.html ; do
  echo "____________________________________"
  echo " checking " $f
  linkchecker -r1 --check-css --check-html $f
done
