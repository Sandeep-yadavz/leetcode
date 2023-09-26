class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n=len(s)
        d={}
        for i in range(n):
            d[s[i]]=i   
        ans=[]
        v={}
        for j in range(n):
            if s[j] not in v: 
                while  ans and ans[-1]>s[j] and d[ans[-1]]>j:
                    x=ans.pop()
                    del v[x]
                ans.append(s[j])
                v[s[j]]=s[j]
        return "".join(ans)          