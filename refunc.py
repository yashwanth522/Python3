#!/usr/bin/python3

import re

line = "cats are smarter than dogs!!"

matchobj = re.match(r'dogs', line, re.M|re.I)

if matchobj:
    print("match object --> ", matchobj.group())
else:
    print("no match!!")

searchobj = re.search(r'dogs', line, re.M|re.I)

if searchobj:
    print("search object --> ", searchobj.group())
else:
    print("nothing found!!")

