s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s = s.lower();

# res = ""
# for char in s:
#     if char.isalpha():
#         res = res + chr( (ord(char) - ord('a') + 2)%26 + ord('a') )
#     else:
#         res = res + char
#
# print(res)


# using str.maketrans() too create a map table
# and use this mal table into translate function.
trans = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
print(s.translate(trans))


# The message is:
# i hope you didnt translate it by hand.
# thats what computers are for.
# doing it in by hand is inefficient and that's why this text is so long.
# using string.maketrans() is recommended. now apply on the url.

print("map".translate(trans))
