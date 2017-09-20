#!/usr/bin/env python3

import io
import os
import time
import yaml
import shutil
from codecs import open
from jinja2 import Environment, FileSystemLoader

jinja_env = Environment(
    keep_trailing_newline = False,
    lstrip_blocks = True,
	trim_blocks = True,
	autoescape = False,
	loader = FileSystemLoader(os.path.abspath('.'))
)

# make the live web directory if needed
# move old to a timestamp just in case
liveweb = './live'

if os.path.exists(liveweb):
    timestamp = time.strftime('%c').replace(' ', '-').replace(':', '.')
    shutil.move(liveweb, liveweb+'-'+timestamp)

os.makedirs(liveweb)

import re
import datetime
urlpattern = re.compile(r'\b(CS|CSE|MATH|ECE)\s*(\d+)')
year = datetime.datetime.now().year

#newurl = ('<a href="https://courses.illinois.edu/'
#  'cisapp/dispatcher/catalog/{year}/fall/%s/%s">%s%s</a>'.format(year=year))
newurl = ('<a href="https://courses.illinois.edu/schedule/terms/%s/%s">%s%s</a>')

def urlify(somestring):
    """
    Takes CS357 and turns it into the URL in newurl
    """
    return urlpattern.sub(newurl%('\g<1>','\g<2>','\g<1>','\g<2>'), somestring)

with open("people.yml", "r", encoding="utf-8") as inf:
  people = yaml.load(inf)

with open("courses.yml", "r", encoding="utf-8") as inf:
  courses = yaml.load(inf)
  courses = [course for course in courses if course['number'] is not None]
  for course in courses:
      course['description'] = [urlify(d) for d in course['description'].split('\n\n')]

print(courses[0])

files = ['_index.html', '_people.html', '_contact.html', '_courses.html']

# now render the pages
for f in files:
    template_vars = {}
    template_vars['people'] = people
    template_vars['courses'] = courses

    template = jinja_env.get_template(f)
    html = template.render(template_vars)
    with io.open(os.path.join('./live/', f[1:]), 'w', encoding='utf8') as fout:
        fout.write(html)

# copy these directories as-is to the webdir
livedirs = ['font-awesome', 'bootstrap', 'css', 'images']
for d in livedirs:
    if os.path.isdir(d):
        shutil.copytree(d, os.path.join(liveweb, d))

# copy these files as-is to the webdir
livefiles = []
for f in livefiles:
    shutil.copyfile(f, os.path.join(liveweb, f))
