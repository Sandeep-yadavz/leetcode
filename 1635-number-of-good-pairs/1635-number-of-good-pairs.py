class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=1+d.get(i,0)
        ans=0
        for i in d:
            if d[i]>1:
                ans+=(d[i]*(d[i]-1))//2
        return ans

        