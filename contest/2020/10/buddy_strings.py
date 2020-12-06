class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        diffs = []
        seen = dict()
        for i in range(len(A)):
            seen[A[i]] = seen.get(A[i], 0) + 1
            if A[i] != B[i]:
                diffs.append(i)
                if len(diffs) > 2:
                    return False
        if len(diffs) == 0:
            for letter in seen:
                if seen[letter] > 1:
                    return True
        if len(diffs) != 2:
            return False
        return A[diffs[0]] == B[diffs[1]] and A[diffs[1]] == B[diffs[0]]
