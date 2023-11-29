import re

"""
In the previous challenge Our Regex match people
who had first name and last name however
if the the first name and lastname contain multiple
whitespaces the Regex will fail

Your mission is to fix
"""


names = ['Finn Bindeballe',
         'George Syslvester Mulbah',
         'HappyCodingRobot',
         'Ron Cromberge',
         'The  Primeagen',
         'Sohil']

regex = r'^\w+\s+\w+$'

for name in names:
    result = re.search(regex, name)
    if result:
        print(name)
