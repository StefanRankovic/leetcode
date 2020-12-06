class Node:
    def __init__(self, val='', word=False):
        self.val = val
        self.word = word
        self.child = []

    def findChild(self, val):
        for c in self.child:
            if c.val == val:
                return c
        return None

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
        node = self.root
        for letter in word:
            next = node.findChild(letter)
            if not next:
                next = Node(letter)
                node.child.append(next)
            node = next
        node.word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for letter in word:
            node = node.findChild(letter)
            if not node:
                return False
        return node.word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for letter in prefix:
            node = node.findChild(letter)
            if not node:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
