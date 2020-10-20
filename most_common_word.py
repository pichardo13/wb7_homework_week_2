"""
https://leetcode.com/problems/most-common-word/description/
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  
The answer is in lowercase.

Example:
Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
"""
from collections import Counter
import re
def mostCommonWord(paragraph, banned):
    #step 1: get rid of all of punctuation and only select the words using re
    p = re.split(r'\W+', paragraph.lower())
    
    #step 2: only select the words that are not in the list of banned words
    words = [w for w in p if w not in banned]
    
    #step 3: using counter count how many times the words appear, using most common return the most common word
    return Counter(words).most_common(1)[0][0]


print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))