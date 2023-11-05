from collections import deque 
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        dq=deque(arr)
        d={}
        ans=0
        for i in range(len(arr)):
            ans=max(ans,arr[i])
            if dq[1]<dq[0]:
                dq[0],dq[1]=dq[1],dq[0]
            temp=dq[0]
            dq.popleft()
            dq.append(temp)
            d[dq[0]]=1+d.get(dq[0],0)
        for i in d:
            if d[i]>=k:
                return i
        
        return ans   
        


        