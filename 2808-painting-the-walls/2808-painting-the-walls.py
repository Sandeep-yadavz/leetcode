class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n=len(cost)
        dp={}
        def helper(i,remain):
            if remain<=0:
                return 0
            if i==n:
                return float('inf')
            if (i,remain) in dp:
                return dp[(i,remain)] 
            include=cost[i]+helper(i+1,remain-1-time[i])
            exclude=helper(i+1,remain)
            dp[(i,remain)]=min(include,exclude)
            return dp[(i,remain)]
        return helper(0,n)

        