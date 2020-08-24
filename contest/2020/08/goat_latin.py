class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        result = ''
        words = S.split()
        for i, word in enumerate(words):
            curr = word
            if len(word) > 1 and word[0] not in vowels:
                curr = word[1:] + word[0]
            curr += 'ma'
            curr += 'a' * (i + 1)
            result += curr
            if i < len(words) - 1:
                result += ' '
        return result
            
