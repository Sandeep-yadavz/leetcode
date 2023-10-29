class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        t=minutesToTest//minutesToDie + 1
        ans=0
        while pow(t,ans)<buckets:
            ans+=1
        return ans