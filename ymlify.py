import yaml
import re

result = []

LINK_RE = re.compile(r"^<a href=\"(.*?)\">(.*?)</a>(.*?)$")

with open("alumni-tmp.txt", "rt") as inf:
    for l in inf:
        l = l.strip()
        if l.endswith("<br>"):
            l = l[:-4]

        l_match = LINK_RE.match(l)
        if l_match:
            person = dict(
                name=l_match.group(2),
                url=l_match.group(1),
                )

            if l_match.group(3).startswith(","):
                deg_data = l_match.group(3)[1:].strip().split()
                person["degree_what"] = deg_data[0]
                person["degree_year"] = int(deg_data[1])

            result.append(person)
        elif l:
            # name, deg_data = l.split(",")
            # deg_data = deg_data.split()
            # person = dict(
            #     name=name,
            #     degree_what=deg_data[0],
            #     degree_year=deg_data[1],
            #     )
            # result.append(person)
            person = dict(name=l)
            result.append(person)

        person["category"] = "former"

print yaml.dump(result, default_flow_style=False)
