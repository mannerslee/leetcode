# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_map = {}
        for index, item in enumerate(inorder):
            inorder_map[item] = index

        def helper(pre_start, in_left, in_right):
            if pre_start >= len(preorder) or in_left > in_right:
                return None

            root = TreeNode(preorder[pre_start])
            root_index = inorder_map[preorder[pre_start]]

            root.left = helper(pre_start + 1, in_left, root_index - 1)
            root.right = helper(pre_start + root_index - in_left + 1, root_index + 1, in_right)

            return root

        return helper(0, 0, len(inorder) - 1)