from typing import List

class Trie:
    def __init__(self):
        # Initialize a Trie node with children for each letter of the alphabet and a flag to mark the end of a word
        self.children = [None] * 26
        self.count = 0

    def insert(self, word):
        # Insert a word into the Trie. Iterate through each character in the word, calculate its index, and create new Trie nodes as necessary.
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
            node.count += 1

    def search(self, word):
        # Search for a word in the Trie. Traverse the Trie based on each character in the word. If we reach the end and the is_end_of_word flag is True, the word exists in the trie.
        node = self
        totalCount = 0
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                return totalCount
            node = node.children[index]
            totalCount += node.count
        return totalCount

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return [trie.search(word) for word in words]
