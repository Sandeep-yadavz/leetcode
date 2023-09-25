class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a=0
        b=0
        for i in s:
            a+=ord(i)
        for j in t:
            b+=ord(j)
        return chr(b-a)
        
            
        