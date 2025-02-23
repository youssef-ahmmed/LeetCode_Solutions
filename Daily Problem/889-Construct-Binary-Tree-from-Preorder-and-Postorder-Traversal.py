# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_idx = {n:i for i, n in enumerate(postorder)}
        tree_val = {preorder[0]:TreeNode(preorder[0])}
        root = tree_val[preorder[0]]

        for i, order in enumerate(preorder):
            left_value = preorder[i + 1] if i + 1 < len(preorder) else None
            if left_value and left_value not in tree_val:
                left = TreeNode(left_value)
                tree_val[order].left = left
                tree_val[left_value] = left

            right_idx = post_idx[order]
            right_value = postorder[right_idx - 1] if right_idx - 1 >= 0 else None
            if right_value and right_value not in tree_val:
                right = TreeNode(right_value)
                tree_val[order].right = right
                tree_val[right_value] = right

        return root
