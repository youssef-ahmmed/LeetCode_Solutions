# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes = []
        i, n = 0, len(traversal)

        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1

            num_start = i
            while i < n and traversal[i].isdigit():
                i += 1

            value = int(traversal[num_start : i])

            nodes.append([TreeNode(value), depth])

        stack = []
        root = nodes[0][0]

        for node, depth in nodes:
            while stack and len(stack) > depth:
                stack.pop()

            if stack:
                parent = stack[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node

            stack.append(node)

        return root
