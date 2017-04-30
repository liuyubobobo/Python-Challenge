fname = "msg.txt"
try:
    fhandle = open(fname)
except:
    print("No such a file:", fname)
    exit()

s = fhandle.read()
res = ""
for c in s:
    if c.isalpha():
        res += c
print(res)