"""
https://leetcode.com/problems/implement-trie-prefix-tree/
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
"""
class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = Node()
            if i == len(word) - 1:
                curr.isEnd = True
            curr = curr.children[word[i]]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for i in range(len(word) - 1):
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True
    
# trie = Trie()

# trie.insert("apple")
# print(trie.search("apple"))  #returns true
# print(trie.search("app"))    #returns false
# print(trie.startsWith("app")) #returns true
# trie.insert("app") 
# print(trie.search("app")) #true

# trie = Trie()
# trie.insert("app")
# trie.insert("apple")
# trie.insert("beer")
# trie.insert("add")
# trie.insert("jam")
# trie.insert("rental")
# trie.search("apps")
# trie.search("app")
# trie.search("ad")
# trie.search("applepie") 
# trie.search("rest")
# trie.search("jan") #wrong answer here, gives T but is F
# trie.search("rent")
# trie.search("beer")
# trie.search("jam")
# trie.startsWith("apps")
# trie.startsWith("app")
# trie.startsWith("ad")
# trie.startsWith("applepie")
# trie.startsWith("rest")
# trie.startsWith("jan")
# trie.startsWith("rent")
# trie.startsWith("beer")
# trie.startsWith("jam")


# ["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search",
# "search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith",
# "startsWith","startsWith","startsWith"]
# [[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],
# ["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]

# [false,true,false,false,false,false,false,true,true,false,true,
# true,false,false,false,true,true,true]