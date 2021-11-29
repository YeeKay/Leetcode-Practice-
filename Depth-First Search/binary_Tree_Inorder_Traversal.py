# Problem description : Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Traversal
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res) # helper function

        return res

    def helper(self, root: Optional[TreeNode], res:List[int]) -> List[int]:
        if root:
            self.helper(root.left, res) # recursively traverse left-child first 
            res.append(root.val)
            self.helper(root.right, res) # recursively traverse right-child 

# Time complexity: O(n)
# Space complexity: O(1)  

# Iterative Traversal
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []

        while True:  
            while root: # iterate all left-children first 
                stack.append(root) 
                root = root.left
            
            if not stack: # no more nodes to be explored
                return res
            
            node = stack.pop() # pop the last element in the stack 
            res.append(node.val)
            root = node.right # iterate right-children 

# Input: root = [1,null,2,3]
# Output: [1,3,2]     

# Input: root = []
# Output: []

# Input: root = [1]
# Output: [1]

# Time complexity: O(n)
# Space complexity: O(n)   