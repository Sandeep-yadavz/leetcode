class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        l=0
        if len(left)!=0:
            l=max(left)
        r=0
        for i in right:
            r=max(n-i,r)
        return max(l,r)