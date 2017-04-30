fname = "msg.txt"
try:
    fhandle = open(fname)
except:
    print("No such a file:", fname)
    exit()

freq = dict()

for line in fhandle:
    line = line.strip()
    for c in line:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1;

for key in freq:
    print(key, freq[key])

fhandle.close()

# equality