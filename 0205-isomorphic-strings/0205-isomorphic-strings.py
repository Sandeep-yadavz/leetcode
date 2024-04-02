class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        v=set()
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in v:
                    return False
                d[s[i]]=t[i]
                v.add(t[i])
                
            else:
                if d[s[i]]!=t[i]:
                    return False
        return True
        