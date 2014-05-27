import re


class newsitem:
    title = None
    date = None
    note = None

title = re.compile('^Title:\s*(.+)')
date = re.compile('^Date:\s*(.+)')
note = re.compile('^Note:\s*(.+)')

current = ''
ni = None

with open('news.txt', 'r') as news:
    with open('news-archive-table.html', 'w') as newshtml:
        newshtml.write('## -*- coding: utf-8 -*-\n')
        newshtml.write('<table>\n')
        for line in news:
            t = title.match(line)
            d = date.match(line)
            n = note.match(line)

            if t:
                # found a new entry/title
                if ni:
                    ni.note = current
                    newshtml.write('<tr>\n')
                    newshtml.write('<td>' + ni.title + '</td>')
                    newshtml.write('<td>' + ni.date + '</td>')
                    newshtml.write('<td>' + ni.note + '</td>\n')
                    newshtml.write('</tr>\n')
                ni = newsitem()
                current = t.group(1)
            elif d:
                # found a date
                ni.title = current
                current = d.group(1)
            elif n:
                # found a date
                ni.date = current
                current = n.group(1)
            else:
                # add to last field
                current += ' ' + line.strip()
        newshtml.write('</table>\n')
