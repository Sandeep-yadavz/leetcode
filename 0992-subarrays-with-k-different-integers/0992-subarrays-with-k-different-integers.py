class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(x):
            i=0
            j=0
            d={}
            n=len(nums)
            res=0
            while j<n:
                d[nums[j]]=1+d.get(nums[j],0)
                j+=1
                if len(d)>x:
                    while i<j and len(d)>x:
                        d[nums[i]]-=1
                        if d[nums[i]]==0:
                            del d[nums[i]]
                        i+=1
                res+=(j-i)
            return res
        return helper(k)-(helper(k-1) if k>1  else 0)                    