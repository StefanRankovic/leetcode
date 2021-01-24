from typing import List
from string import ascii_lowercase
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque([(beginWord, 1)])
        while queue:
            word, wlen = queue.popleft()
            for i in range(len(word)):
                for c in ascii_lowercase:
                    next = word[:i] + c + word[i+1:]
                    if next in wordList:
                        if next == endWord:
                            return wlen+1
                        wordList.remove(next)
                        queue.append((next, wlen+1))
        return 0
