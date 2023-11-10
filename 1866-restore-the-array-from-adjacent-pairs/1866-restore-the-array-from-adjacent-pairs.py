class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d={}
        for i in adjacentPairs:
            if i[0] not in d:
                d[i[0]]=[]
            if i[1] not in d:
                d[i[1]]=[]
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        ans=[]
        s=set()
        for i in d:
            if len(d[i])==1:
                temp=i
                break
        while len(ans)!=len(adjacentPairs)+1:
            ans.append(temp)
            s.add(temp)
            for i in d[temp]:
                if i not in s:
                    temp=i
        return ans

        