class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        iso = {}
        for i in range(len(s)):
            if s[i] in iso: 
                if iso[s[i]] != t[i]:
                    return False
            else:
                if t[i] in iso.values():
                    return False
                iso[s[i]] = t[i]
        return True
            
        
