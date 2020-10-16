"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
"""
def uncommonFromSentences(A, B):
    wordCounts = {}
    uncommonWords = []

    for i in A.split(' '):
        if i not in wordCounts:
            wordCounts[i] = 1
        else:
            wordCounts[i] += 1

    
    for j in B.split(' '):
        if j not in wordCounts:
            wordCounts[j] = 1
        else:
            wordCounts[j] += 1
    
    for word in wordCounts:
        if wordCounts[word] == 1:
            uncommonWords.append(word)
    return uncommonWords

print(uncommonFromSentences("apple apple", "banana"))
print(uncommonFromSentences("this apple is sweet", "this apple is sour"))

