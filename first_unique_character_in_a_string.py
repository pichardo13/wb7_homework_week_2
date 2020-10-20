"""
https://leetcode.com/problems/first-unique-character-in-a-string/description/
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Example 1:
s = "leetcode"
return 0.

Example 2:
s = "loveleetcode"
return 2.
"""
import collections
def firstUniqChar(s):
    #count each char in string
    c = collections.Counter(s)

    #for each char
    for i in c:
        #if count of char == 1
        if c[i] == 1:
            #return the index where this char is found in s
            return s.index(i)
    return -1

print(firstUniqChar('leetcode'))
print(firstUniqChar('loveleetcode'))