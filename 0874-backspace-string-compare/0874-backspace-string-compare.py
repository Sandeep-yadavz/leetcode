class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            if i=='#':
                if len(a)!=0:
                    a.pop()
            else:
                a.append(i)
        for i in t:
            if i=='#':
                if len(b)!=0:
                    b.pop()
            else:
                b.append(i)
        return a==b