import yaml
from yaml.loader import SafeLoader
from yaml.loader import FullLoader

# Open the file and load the file
with open('verify_apache.yaml') as f:
    docs = list(yaml.safe_load_all(f))
dicti = docs[0][0]
print(dicti)


members = [{'name': 'Zoey', 'occupation': 'Doctor'},
           {'name': 'Zaara', 'occupation': 'Dentist'}]

with open('sample.yaml', 'w') as f:
    yaml.dump_all(members, f)

