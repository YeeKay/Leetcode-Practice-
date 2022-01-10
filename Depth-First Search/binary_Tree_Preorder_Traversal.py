# Problem Description: Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative Traversal:

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [root]

        while stack:
            node = stack.pop()

            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            
        return res

# Time complexity: O(n)
# Space complexity: O(n)

# Recursive Traversal 

# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         self.helper(root, res)

#         return res
#         # if not root.left and not root.right: # base case: leaf
#         #     return root.val
        
#         # ans.append(self.preorderTraversal(root))
        
#         # if root.left:
#         #     ans.append(self.preorderTraversal(root.left))

#         # if root.right:
#         #     ans.append(self.preorderTraversal(root.right))
    
#     def helper(self, root: Optional[TreeNode], res: List[int]) -> List[int]:
#         if root:
#             res.append(root.val)
#             self.helper(root.left, res)
#             self.helper(root.right, res)


# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Input: root = []
# Output: []

# Input: root = [1]
# Output: [1]