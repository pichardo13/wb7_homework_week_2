"""
https://leetcode.com/problems/find-the-difference/description/
You are given two strings s and t.
String t is generated by random shuffling string s and then add one more letter at a random position.
Return the letter that was added to t.

Example 1:
Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

Example 2:
Input: s = "", t = "y"
Output: "y"

Example 3:
Input: s = "a", t = "aa"
Output: "a"

Example 4:
Input: s = "ae", t = "aea"
Output: "a"
"""
def findTheDifference(s,t):
    for i in set(t):
        if t.count(i) != s.count(i):
            return i
    

print(findTheDifference("abcd", "abcde"))
print(findTheDifference("", "y"))
print(findTheDifference("a", "aa"))
print(findTheDifference("ae", "aea"))