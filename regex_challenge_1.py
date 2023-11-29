import re

names = ['Finn Bindeballe',
         'George Syslvester Mulbah',
         'HappyCodingRobot',
         'Ron Cromberge',
         'Sohil']

# challenge Create a regex that find people who have only their first
# and last name

regex = r'^\w+ \w+$'

for name in names:
    result = re.search(regex, name)
    if result:
        print(name)
