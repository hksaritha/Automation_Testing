'''
1. Match is used to find a pattern from starting positon
'''
import re

name = 'sriram'

mo = re.match('sri', name)
print(mo.group())


