import queue
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        d=defaultdict(list)
        degree=[0 for j in range(n)]
        for i in relations:
            degree[i[1]-1]+=1
            d[i[0]-1].append(i[1]-1)
        max_time=[]
        q=queue.Queue()
        for j in range(n):
            if degree[j]==0:
                q.put(j)
            max_time.append(time[j])
        while not q.empty():
            curr=q.get()
            for nxt in d[curr]:
                max_time[nxt]=max(max_time[nxt],max_time[curr]+time[nxt])
                degree[nxt]-=1
                if degree[nxt]==0:
                    q.put(nxt)
        return max(max_time)

