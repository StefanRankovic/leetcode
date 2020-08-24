class Trie:
    def __init__(self, val=None):
        self.val = val
        self.children = dict()
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        def add(node, word, i):
            if word[i] not in node.children:
                node.children[word[i]] = Trie(word[i])
            if i + 1 == len(word):
                node.children[word[i]].end = True
            else:
                add(node.children[word[i]], word, i + 1)
        add(self.root, word, 0)
        

    def search(self, word: str) -> bool:
        def search(node, word, i):
            if i == len(word):
                return node.end
            elif word[i] == '.':
                for c in node.children:
                    res = search(node.children[c], word, i + 1)
                    if res:
                        return True
            elif word[i] not in node.children:
                return False
            else:
                return search(node.children[word[i]], word, i + 1)
        return search(self.root, word, 0)
            
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
