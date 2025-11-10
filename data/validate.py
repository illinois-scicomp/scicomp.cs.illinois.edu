import yaml

with open("people.yml", "r", encoding="utf-8") as inf:
    people = yaml.load(inf, Loader=yaml.FullLoader)

person_template = people.pop(0)

# check required fields
for person in people:
    for key in ['name', 'category', 'status']:
        if not person.get(key):
            print(f'missing "{key}" in "{person['name']}"')

# check fields are valid
for person in people:
    for key in person.keys():
        if key not in person_template.keys():
            print(f'invalid "{key}" in "{person['name']}"')

# year_arrived
for person in people:
    if person.get('year_arrived'):
        if person['category'] not in ['faculty', 'postdoc', 'staff', 'visiting scholar']:
            print(f'year_arrived not valid for "{person['name']}"')

# year_left
for person in people:
    if person.get('year_left'):
        if person['category'] in ['faculty', 'postdoc', 'staff', 'visiting scholar']:
            if person['status'] != 'former':
                print(f'year_left not valid for "{person['name']}"')
        else:
            print(f'year_left not valid for "{person['name']}"')

# degree_
for person in people:
    if person.get('degree_what') or person.get('degree_year'):
        if person['category'] not in ['grad', 'undergrad']:
            print(f'degree_* not valid for "{person['name']}"')

# thesis_
for person in people:
    if person.get('thesis_what') or person.get('thesis_year'):
        if person['category'] not in ['grad', 'undergrad']:
            print(f'thesis_* not valid for "{person['name']}"')
