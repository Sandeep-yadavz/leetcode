# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        global ans
        ans=0
        def helper(root):
            global ans
            if root==None:
                return (0,0)
            l=helper(root.left)
            r=helper(root.right)
            tree_sum=l[0]+r[0]+root.val
            no_nodes=l[1]+r[1]+1
            if tree_sum//no_nodes==root.val:
                ans+=1
            return (tree_sum,no_nodes)
        helper(root)
        return ans
        