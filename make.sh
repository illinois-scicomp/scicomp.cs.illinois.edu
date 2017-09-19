#! /bin/bash

set -e
set -x

mkdir -p live/images/people/scaled
for f in ./live/images/people/*jpeg; do
  dn=$(dirname $f)
  bn=$(basename $f)
  scaled="$dn/scaled/$bn"
  if [ "$f" -nt "$scaled" ] || [ "${0}" -nt "$scaled" ]; then
    #convert -geometry 500x500 "$f" "$scaled"
    convert -resize 360x500^ -gravity center -extent 360x500 "$f" "$scaled"
  fi
done

#rm -f live/*.html

#for i in *.html ; do
#  python3 render.py $i live/$i
#done
