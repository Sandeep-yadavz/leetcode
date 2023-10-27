class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(i,j):
            x=s[i:j+1]
            return x==x[::-1]
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=[]
            d[s[i]].append(i)
        ans=s[0]
        print(d)
        for i in d:
            if len(d[i])==1:
                continue
            for j in range(len(d[i])):
                for k in range(j+1,len(d[i])):
                    x,y=d[i][j],d[i][k]
                    if y-x+1>len(ans):
                        if helper(x,y):    
                            ans=s[x:y+1]
                    else:
                        continue
        return ans
        