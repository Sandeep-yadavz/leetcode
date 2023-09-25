class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for i in s:
            d[i]=1+d.get(i,0)
        d2={}
        for j in t:
            d2[j]=1+d2.get(j,0)
        for k in d2:
            if k not in d or d[k]!=d2[k]:
                return k
        
            
        