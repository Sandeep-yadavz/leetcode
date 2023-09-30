class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mini=nums[0]
        stack=[]
        for i in nums:
            while stack and stack[-1][0]<=i:
                stack.pop()
            if stack and stack[-1][1]<i:
                return True
            stack.append([i,mini])
            mini=min(i,mini)
        return False