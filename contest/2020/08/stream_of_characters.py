from typing import List

class Trie:
    def __init__(self, end=False):
        self.child = dict()
        self.end = end

    def add(self, word, i=0):
        if word[i] not in self.child:
            self.child[word[i]] = Trie()
        if i == len(word) - 1:
            self.child[word[i]].end = True
            return
        self.child[word[i]].add(word, i + 1)

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        for word in words:
            self.root.add(word[::-1])
        self.stream = ''

    def query(self, letter: str) -> bool:
        self.stream = letter + self.stream
        ptr = self.root
        for c in self.stream:
            if c not in ptr.child:
                break
            ptr = ptr.child[c]
            if ptr.end:
                return True
        return False
