class Solution:
    def countHomogenous(self, s: str) -> int:
        d={}
        s+=" "
        temp=""
        mod=10**9+7
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                temp+=s[i]
            else:
                temp+=s[i]
                d[temp]=1+d.get(temp,0)
                temp=""
        ans=0
        for i in d:
            ans+=(d[i])*(len(i)*(len(i)+1)//2)%mod
        return ans

        