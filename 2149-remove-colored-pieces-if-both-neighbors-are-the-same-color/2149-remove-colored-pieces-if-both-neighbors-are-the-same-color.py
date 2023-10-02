import heapq
class Solution:
    def winnerOfGame(self, c: str) -> bool:
        a=[]
        b=[]
        prv=c[0]
        cnt=1
        c+=" "
        for i in range(1,len(c)):
            if prv==c[i]:
                cnt+=1
            else:
                if prv=='A':
                    if cnt>=3:
                        heapq.heappush(a,cnt)
                else:
                    if cnt>=3:
                        heapq.heappush(b,cnt)
                prv=c[i]
                cnt=1
        print(a,b)
        while a and b:
            x=heapq.heappop(a)
            if x-1>=3:
                heapq.heappush(a,x-1)
            y=heapq.heappop(b)
            if y-1>=3:
                heapq.heappush(b,y-1)
        if len(a)==0 and len(b)==0:
            return False
        if len(a)==0 and len(b)!=0:
            return False
        if len(a)!=0 and len(b)==0:
            return True


        