#! /bin/bash

set -e
set -x

rm -f live/*.html

for i in *.html ; do
  python render.py $i live/$i
done
