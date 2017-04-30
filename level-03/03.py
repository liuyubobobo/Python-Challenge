fname = "msg.txt"
try:
    fhandle = open(fname)
except:
    print("No such a file:", fname)
    exit()


def cut_line(line):
    line = line.strip()

    res = []
    start = 0
    index = 1
    while index <= len(line):
        if index == len(line) or line[index].isupper() != line[start].isupper():
            res.append(line[start:index])
            start = index
            index += 1
        else:
            index += 1

    return res


def fit_pattern(arr):

    if len(arr) != 3:
        return False
    for i in range(3):
        if not isinstance(arr[i], str):
            return False
    if arr[0][0].islower() or len(arr[0]) != 3:
        return False
    if arr[1][0].isupper() or len(arr[1]) != 1:
        return False
    if arr[2][0].islower() or len(arr[2]) != 3:
        return False

    return True


res = ""

for line in fhandle:
    segs = cut_line(line)
    for i in range(len(segs)-3+1):
        if fit_pattern(segs[i:i+3]):
            res += segs[i+1]

print(res)
# linkedlist
