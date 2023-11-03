class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        i=0
        for j in range(1,n+1):
            if j==target[i]:
                res.append('Push')
                i+=1
                if i==len(target):
                    break
            else:
                res.append('Push')
                res.append('Pop')
        return res

