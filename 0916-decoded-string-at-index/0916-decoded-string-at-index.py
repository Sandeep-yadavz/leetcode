class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        cnt=0
        i=0
        n=len(s)
        while i<n:
            if '2'<=s[i]<='9':
                if (int(s[i])-1)*cnt>=k:
                    i=0
                    cnt=0
                    continue
                else:
                    k-=(int(s[i])-1)*cnt
                    cnt+=(int(s[i])-1)*cnt
            else:
                k-=1
                cnt+=1
                if k==0:
                    return s[i]
            i+=1
            

    