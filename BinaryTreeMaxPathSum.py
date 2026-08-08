# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #kadane Alg

        self.res = root.val

        def dfs(node):

            if not node:
                return 0
            left = right = 0

            left = max(left, dfs(node.left))
            right = max(right, dfs(node.right))

            self.res = max(self.res, left+node.val+right)
            return node.val+max(left, right)    
        dfs(root)

        return self.res    
        