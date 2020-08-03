class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        cap1 = word[0].isupper()
        cap2 = word[1].isupper()
        if not cap1 and cap2:
            return False
        if len(word) == 2:
            return True
        return all([x.isupper() if cap1 and cap2 else x.islower() for x in word[2:]])
            
