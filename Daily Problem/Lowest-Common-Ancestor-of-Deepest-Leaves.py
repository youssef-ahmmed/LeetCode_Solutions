# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return (None, 0)

            left, left_height = dfs(node.left)
            right, right_height = dfs(node.right)

            if left_height == right_height:
                return node, left_height + 1
            elif left_height > right_height:
                return left, left_height + 1
            else:
                return right, right_height + 1

        node, _ = dfs(root)
        return node
