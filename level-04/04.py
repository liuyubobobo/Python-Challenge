import urllib.request
import re

#number = "12345"
# We'll go to nothing = 16044 and get "Yes. Divide by two and keep going."

#number = "8022"
# We'll go to nothing = 82682 and get:
# There maybe misleading numbers in the text. One example is 82683.
# Look only for the next nothing and the next nothing is 63579

number = "63579"

while True:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + number
    handle = urllib.request.urlopen(url)
    s = handle.read().decode()
    res = re.findall("[0-9]+", s)
    if len(res) == 0:
        print(s)
        break

    try:
        assert len(res) == 1
    except:
        print("More than one number occurred in the page:", url)
        print(s)
        break

    print(res[0])
    number = res[0]

# At last, when nothing = 66831, we get "peak.html" :)