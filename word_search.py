"""
https://leetcode.com/problems/word-search-ii/
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" 
cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
"""
class Node:
    def __init__(self):
        self.children = {}

class TrieTree:
    def __init__(self):
        self.root = None
    
    def insert(self, words):
        return 

"""
Plan: 
Step 1: Make a trie tree with the words from the words list.
Step 2: Traverse board, as traversing if the character matches then traverse down trie tree.
Step 3: If word found on board add to a result list
Step 4: Return result list with words
"""
def findWords(board, words):
    return