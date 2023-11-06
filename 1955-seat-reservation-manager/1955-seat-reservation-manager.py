import heapq
class SeatManager:

    def __init__(self, n: int):
        self.q=[i for i in range(1,n+1)]
        self.d={}

    def reserve(self) -> int:
        x=heapq.heappop(self.q)
        self.d[x]=1
        return x

        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.q,seatNumber)
        del self.d[seatNumber]
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)