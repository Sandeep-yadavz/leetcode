class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                break
        f=nums[i]>nums[i+1]
        print(i)
        for j in range(i,len(nums)-1):
            if nums[j]==nums[j+1]:
                continue
            x=nums[j]>nums[j+1]
            if x!=f:
                return False
        return True        