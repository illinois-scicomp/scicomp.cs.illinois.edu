#! /bin/bash

set -e
set -x

rm -f live/*.html

for i in index.html ; do
  mako-render $i > live/$i
done
