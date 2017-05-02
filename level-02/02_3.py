fname = "msg.txt"
try:
    fhandle = open(fname)
except:
    print("No such a file:", fname)
    exit()

s = fhandle.read()

import re
res = re.sub("[^a-z]", "", s)
print(res)

res = re.findall("[a-z]", s)
print("".join(res))