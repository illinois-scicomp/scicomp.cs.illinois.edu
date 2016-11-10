from mako.template import Template
from mako.lookup import TemplateLookup

import sys
from codecs import open

lookup = TemplateLookup(["."])
with open(sys.argv[1], "r", encoding="utf-8") as inf:
    tpl = Template(
        inf.read(),
        lookup=lookup,
        strict_undefined=True)
    with open(sys.argv[2], "w", encoding="utf-8") as outf:
        outf.write(tpl.render(
            SOURCES=[("page template", sys.argv[1])],
            ))
