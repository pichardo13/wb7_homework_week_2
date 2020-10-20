"""
https://leetcode.com/problems/sort-characters-by-frequency/description/
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
Input:
"tree"
Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input:
"cccaaa"
Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input:
"Aabb"
Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
from collections import Counter
def frequencySort(s):
    #Step 1: counter will count the number of characters in string (hashmap/dict)
    #Step 2: .most_common() will return a list of tuples sorted by values
    #Step 3: multiple the char * count (i[0] * i[1] == ("v", 4) from Counter(s).most_common)
    #Step 4: list comprehension results joined into a string
    return ''.join(i[0] * i[1] for i in Counter(s).most_common())

print(frequencySort("Aabb"))
print(frequencySort("cccaaa"))
print(frequencySort("tree"))