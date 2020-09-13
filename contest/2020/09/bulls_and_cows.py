class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        marker = list(secret)
        cntA = cntB = 0
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                marker[i] = 'A'
                cntA += 1
        for i in range(len(guess)):
            if marker[i] == 'A':
                continue
            for j in range(len(marker)):
                if guess[i] == marker[j]:
                    marker[j] = 'B'
                    cntB += 1
                    break
        return f'{cntA}A{cntB}B'
