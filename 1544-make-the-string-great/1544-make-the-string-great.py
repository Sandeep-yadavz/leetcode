class Solution:
    def makeGood(self, s: str) -> str:
        a=[]
        for i in s:
            if len(a)==0:
                a.append(i)
            else:
                if i.isupper():
                    if i.lower()==a[-1]:
                        a.pop()
                    else:
                        a.append(i)
                else:
                    if i.upper()==a[-1]:
                        a.pop()
                    else:
                        a.append(i)
        x=''               
        for j in a:
            x+=j
        return x
                        
        
        