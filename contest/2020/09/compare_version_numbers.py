class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(v) for v in version1.split('.')]
        v2 = [int(v) for v in version2.split('.')]
        n = max(len(v1), len(v2))
        if len(v1) < n:
            v1.extend([0] * (n - len(v1)))
        if len(v2) < n:
            v2.extend([0] * (n - len(v2)))
        for i in range(n):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0
