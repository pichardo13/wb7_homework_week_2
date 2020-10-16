"""
https://leetcode.com/problems/word-pattern/description/
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", s = "dog dog dog dog"
Output: false
"""
def wordPattern(pattern, s):
    patternMap = {}
    sList = s.split(' ')

    if len(pattern) != len(sList):
        return False
    for i in range(len(pattern)):
        if pattern[i] in patternMap and patternMap[pattern[i]] != sList[i]:
            return False
        patternMap[pattern[i]] = sList[i]
    
    return len(patternMap.keys()) == len(set(patternMap.values()))

print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("aaaa", "dog cat cat dog"))
print(wordPattern("abba", "dog dog dog dog"))
print(wordPattern("aaa", "aa aa aa aa"))