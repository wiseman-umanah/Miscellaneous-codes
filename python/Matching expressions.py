import re

consonantRegex = re.compile(r'[aeiouAEIOU]')
s = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(s)
