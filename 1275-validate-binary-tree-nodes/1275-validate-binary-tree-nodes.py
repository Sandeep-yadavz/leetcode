import queue
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        if n<=1:
            return True
        q=queue.Queue()
        d={}
        for i in range(n):
            if leftChild[i]!=-1:
                d[leftChild[i]]=i
            if rightChild[i]!=-1:
                d[rightChild[i]]=i
        for j in range(n):
            if j not in d:
                q.put(j)
                break
        visited=set()
        count=0
        while not q.empty():
            curr=q.get()
            if curr in visited:
                return False

            visited.add(curr)
            count+=1
            if leftChild[curr]!=-1:
                q.put(leftChild[curr])
            if rightChild[curr]!=-1:
                q.put(rightChild[curr])
        return count==n
        