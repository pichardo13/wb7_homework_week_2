"""
https://leetcode.com/problems/isomorphic-strings/description/
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true
"""

#goal: map each letter in s to it's perspective letter in t, if not consistent return False
def isIsomorphic(s, t):
    stringMap = {}
    for i in range(len(s)):
        if s[i] in stringMap and stringMap[s[i]] != t[i]:
            return False
        stringMap[s[i]] = t[i]
    return len(set(stringMap.keys())) == len(set(stringMap.values())) 
    

print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("ab", "aa"))
