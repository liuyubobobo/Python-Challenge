## Level 4

url: [http://www.pythonchallenge.com/pc/def/linkedlist.php](http://www.pythonchallenge.com/pc/def/linkedlist.php)

**Solution**:

First of all, the hidden message is also in the page's source, which is:

> urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough.

Then, there's a link, which is [linkedlist.php?nothing=12345](linkedlist.php?nothing=12345). We can see there's one more paramether in the address named "nothing". Try to visit the address, we can get a msg, which is:

> and the next nothing is 44827

We can then use the new "nothing" argument to continue and continue. We obsolutely can write a program to repeat the process to find and try new nothing numbers.

The first time we cannot get a nothing number occurred when nothing = 16044 and we got:

> Yes. Divide by two and keep going.

I tried the new nothing number which is 16044 / 2 = 8022 and continue, then we'll go to someplace there're more than one number in the page. That occurred when nothing = 82682 and we got:

> There maybe misleading numbers in the text. One example is 82683. Look only for the next nothing and the next nothing is 63579

I used 63579 as the new nothing number, at last, we got "peak.html" when nothing = 66831 :)

**Code Word for Next Challenge**: peak

**Official solution**: [level 4](http://www.pythonchallenge.com/pcc/def/peak.html)