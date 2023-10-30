class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def helper(x):
            c=0
            i=0
            while x>=(1<<i):
                if (x&(1<<i))>0:
                    c+=1
                i+=1
            return c
        a=[]
        for i in arr:
            a.append([helper(i),i])
        a.sort()
        res=[]
        for i in a:
            res.append(i[1])
        return res

        