class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        res=1
        ans=0
        while j<len(nums):
            res*=nums[j]
            while i<=j  and res>=k:
                res//=nums[i]
                i+=1
            ans+=(j-i)+1
            j+=1
        return ans

        