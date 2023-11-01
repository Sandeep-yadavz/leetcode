# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        q=queue.Queue()
        q.put(root)
        c=0
        d={}
        while not q.empty():
            curr=q.get()
            d[curr.val]=1+d.get(curr.val,0)
            
            if curr.left!=None:
                q.put(curr.left)
            if curr.right!=None:
                q.put(curr.right)
        res=max(d.values())
        ans=[]
        for i in d:
            if d[i]==res:
                ans.append(i)
        return ans

        