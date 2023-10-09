class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=[-1,-1]
        i=0
        j=len(nums)-1
        while i<=j:
            if a[0]!=-1 and a[1]!=-1:
                break
            if nums[i]==target:
                if a[0]==-1:
                    a[0]=i
            else:
                i+=1
            if nums[j]==target:
                if a[1]==-1:
                    a[1]=j
            else:
                j-=1
        return a