## Level 2

url: [http://www.pythonchallenge.com/pc/def/ocr.html](http://www.pythonchallenge.com/pc/def/ocr.html)

**Solution**:

First of all, I check the page souce of the level 2 chanllenge page and can find the msg easily. I stored the msg in a text file [here](https://github.com/liuyubobobo/Python-Challenge/blob/master/level-02/msg.txt).

In [solution 1](https://github.com/liuyubobobo/Python-Challenge/blob/master/level-02/02.py), I used a dictionary to see every character's frequency, and can easily find out only some characters occured once, which can spell to a word: equality. (Thanks to the word has no repeated character. But it's also a unsafe method, since the dictionary is unordered.)

In [solution 2](https://github.com/liuyubobobo/Python-Challenge/blob/master/level-02/02_2.py), I just easily keep all characters and throw other meaningless sign characters away. Then, I can get the key word: equality:)

**Code Word for Next Challenge**: equality

**Official solution**: [level 2](http://wiki.pythonchallenge.com/index.php?title=Level2:Main_Page)