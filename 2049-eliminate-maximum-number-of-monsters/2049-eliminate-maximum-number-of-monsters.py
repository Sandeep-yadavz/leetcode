class Solution:
    def eliminateMaximum(self, d: List[int], s: List[int]) -> int:
        res=[]
        for i in range(len(d)):
            x=d[i]//s[i]
            y=d[i]%s[i]
            if y!=0:
                x+=1
            res.append(x)
        res.sort()
        for i in range(1,len(d)+1):
            if res[i-1]<i:
                if i==1:
                    return 1
                else:
                    return i-1
   
        return len(d)

        