class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(n,k):
            if n==1 and k==1:
                return True
            elif n==2:
                if k==1:
                    return True
                else:
                    return False

            mid=pow(2,n-1)//2
            if k<=mid:
                return helper(n-1,k)
            else:
                return not helper(n-1,k-mid)
        if helper(n,k):
            return 0
        else:
            return 1
            