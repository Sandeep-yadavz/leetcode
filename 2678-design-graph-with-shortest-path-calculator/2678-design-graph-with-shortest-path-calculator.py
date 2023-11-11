import heapq
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.d={i:[] for i in range(n)}
        for i in edges:
            self.d[i[0]].append((i[1],i[2]))
        

    def addEdge(self, edge: List[int]) -> None:
        self.d[edge[0]].append((edge[1],edge[2]))
        
    def shortestPath(self, node1: int, node2: int) -> int:
        dic={}
        dic[node1]=0
        heap=[(0,node1)]
        while heap:
            a,b=heapq.heappop(heap)
            if b==node2:
                return a
            for i in self.d[b]:
                if i[0] not in dic:
                    dic[i[0]]=a+i[1]
                    heapq.heappush(heap,(dic[i[0]],i[0]))
                else:
                    if dic[i[0]]>a+i[1]:
                        dic[i[0]]=a+i[1]
                        heapq.heappush(heap,(dic[i[0]],i[0]))
        return -1

                    
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)