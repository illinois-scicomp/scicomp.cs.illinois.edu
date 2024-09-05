import yaml

with open("people.yml", "r", encoding="utf-8") as inf:
    people = yaml.load(inf, Loader=yaml.FullLoader)

# check required fields
for person in people[1:]:
    for key in ['name', 'category', 'status']:
        if not person.get(key):
            print(f'missing {key} in {person['name']}')
