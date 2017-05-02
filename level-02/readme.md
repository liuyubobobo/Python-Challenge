## Level 2

url: [http://www.pythonchallenge.com/pc/def/ocr.html](http://www.pythonchallenge.com/pc/def/ocr.html)

**Solution**:

First of all, I check the page souce of the level 2 chanllenge page and can find the msg easily. I stored the msg in a text file [here](https://github.com/liuyubobobo/Python-Challenge/blob/master/level-02/msg.txt).

In [solution 1](https://github.com/liuyubobobo/Python-Challenge/blob/master/level-02/02_1.py), I used a dictionary to see every character's frequency, and can easily find out only some characters occured once, which can spell to a word: equality. (Thanks to the word has no repeated character. But it's also a unsafe method, since the dictionary is unordered.)

In [solution 2](https://github.com/liuyubobobo/Python-Challenge/blob/master/level-02/02_2.py), I just easily kept all characters and throw other meaningless sign characters away. Then, I can get the key word: equality:)

In [solution 3](https://github.com/liuyubobobo/Python-Challenge/blob/master/level-02/02_3.py), I used regular expression to find the keyword. I used two way to do that. For one way, I replace every non-alphabeta characters into empty and the remain characters formed the keyword; For another way, I find all alphabeta characters in the message and joined them together to get the keyword.

**Code Word for Next Challenge**: equality

**Official solution**: [level 2](http://www.pythonchallenge.com/pcc/def/equality.html)