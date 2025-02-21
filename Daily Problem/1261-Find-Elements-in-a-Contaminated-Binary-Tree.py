# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.root = root
        self.contaminate_tree(self.root)

    def contaminate_tree(self, root):
        if not root:
            return

        if root.left:
            root.left.val = 2 * root.val + 1
            self.contaminate_tree(root.left)
        if root.right:
            root.right.val = 2 * root.val + 2
            self.contaminate_tree(root.right)

    def find(self, target: int) -> bool:
        return self.search(self.root, target)

    def search(self, root, target):
        if not root:
            return found
 
        found = target == root.val

        if not found and root.left:
            found = self.search(root.left, target)
        if not found and root.right:
            found = self.search(root.right, target)
        
        return found




# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)