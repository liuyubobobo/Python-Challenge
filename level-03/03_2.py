fname = "msg.txt"
try:
    fhandle = open(fname)
except:
    print("No such a file:", fname)
    exit()

import re

msg =fhandle.read()
res = re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", msg)

print("".join(res))
# linkedlist
