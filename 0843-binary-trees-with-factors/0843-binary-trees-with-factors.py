class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        d={}
        ans=0
        for i in arr:
            temp=1
            for j in arr:
                if j>i:
                    break
                temp+=(d.get(j,1)*d.get(i/j,0))
            d[i]=temp
            
        return sum(d.values())%(10**9+7)

        