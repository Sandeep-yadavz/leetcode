class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp={}
        mod=10**9+7
        def helper(i,steps):
            if i>steps or not 0<=i<arrLen:
                return 0
            if steps==0 and i==0:
                return 1
            if (i,steps) in dp:
                return dp[(i,steps)]
            a=helper(i-1,steps-1)
            b=helper(i+1,steps-1)
            c=helper(i,steps-1)
            dp[(i,steps)]=(a+b+c)%(mod)
            return dp[(i,steps)]
        return helper(0,steps)


        