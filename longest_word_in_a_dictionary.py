"""
https://leetcode.com/problems/longest-word-in-dictionary/
Given a list of strings words representing an English Dictionary, find the longest word in words that can be 
built one character at a time by other words in words. If there is more than one possible answer, return the 
longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
"""
class Node:
    def __init__(self):
        self.children = {}
        self.word = None

class TrieTree:
    def __init__(self):
        self.root = Node()
    
    def tree(self):
        return self.root

    def addWord(self, word):
        curr = self.root

        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = Node()
            if i == len(word) - 1:
                curr.word = word
            curr = curr.children[word[i]]
    
    def addWords(self, words):
        for word in words:
            self.addWord(word)

    def longestWord(self):
        word = ""
        stack = [self.root]
        count = 0

        while stack:
            curr = stack.pop()
            for k in curr.children:
                if curr.word:
                    stack.append(curr.children[k])
                    if len(word) == len(curr.word):
                        word = min(word, curr.word)
                    else:
                        #error is here because will compare latte & "mo" and set max word to "mo" bc m > l
                        word = max(word, curr.word)
        return word


def longestWord(words):
    trie = TrieTree()
    trie.addWords(words)
    return trie.longestWord()

print(longestWord(["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]))
#contains bug, should return latte but return mocha


