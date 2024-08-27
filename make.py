#!/usr/bin/env python3

import io
import os
import time
import yaml
import shutil
import re
import datetime
from codecs import open
import unicodedata
import requests
from bs4 import BeautifulSoup
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

urlpattern = re.compile(r'\b(CS|CSE|MATH|ECE)\s*(\d+)')
year = datetime.datetime.now().year

def get_course_description(courses):
    res = requests.get('http://catalog.illinois.edu/courses-of-instruction/cs/')
    soup = BeautifulSoup(res.text, 'html.parser')
    cbs = soup.find_all("div", {"class": "courseblock"})
    for cb in cbs:
        title = cb.find("p", {"class": "courseblocktitle"})
        desc = cb.find("p", {"class": "courseblockdesc"})
        title = unicodedata.normalize("NFKD", title.text)
        desc = unicodedata.normalize("NFKD", desc.text)
        for course in courses:
            if course['number'] in title.replace(' ', ''):
                credit = title.split('credit:')[1]
                credit = 'Credit: ' + credit
                if 'description' not in course:
                    course['description'] = ''
                course['description'] = credit + '\n' + course['description']
                course['description'] += "\n<b>From the course catalog:</b>\n"
                course['description'] += desc

def urlify(somestring):
    """
    Takes CS357 and turns it into the URL in newurl
    """
    newurl = ('<a href="https://courses.illinois.edu/schedule/terms/%s/%s">%s%s</a>')
    return urlpattern.sub(newurl%(r'\g<1>',r'\g<2>',r'\g<1>',r'\g<2>'), somestring)

with open("./data/people.yml", "r", encoding="utf-8") as inf:
    people = yaml.load(inf, Loader=yaml.FullLoader)

with open("./data/courses.yml", "r", encoding="utf-8") as inf:
    courses = yaml.load(inf, Loader=yaml.FullLoader)
    courses = [course for course in courses if course['number'] is not None]
    get_course_description(courses)

for course in courses:
    course['url'] = f"https://courses.illinois.edu/schedule/terms/CS/{course['number'][2:]}"
    course['description'] = [urlify(d) for d in course['description'].split('\n\n')]

files = ['_index.html', '_people.html', '_contact.html', '_courses.html', '_study.html']

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
livedirs = ['css', 'images']
for d in livedirs:
    if os.path.isdir(d):
        shutil.copytree(d, os.path.join(liveweb, d))

# copy these files as-is to the webdir
livefiles = []
for f in livefiles:
    shutil.copyfile(f, os.path.join(liveweb, f))
