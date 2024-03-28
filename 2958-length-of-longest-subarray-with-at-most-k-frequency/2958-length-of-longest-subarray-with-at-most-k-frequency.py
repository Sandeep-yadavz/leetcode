class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        d={}
        res=0
        temp=0
        while j<len(nums):
            d[nums[j]]=1+d.get(nums[j],0)
            temp+=1
            while i<j and d[nums[j]]>k:
                d[nums[i]]-=1
                temp-=1
                if d[nums[i]]==0:
                    del d[nums[i]]
                i+=1
            res=max(res,temp)
            j+=1
        return res
        