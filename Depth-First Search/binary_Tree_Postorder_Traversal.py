# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# left -> right -> root
# Flag method 
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [(root, False)]

        while stack:
            node, visited = stack.pop()

            if node:
                if visited:
                    res.append(node.val)

                # post-order
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return res
    

# modify pre-order from root-left-right to root-right-left and reverse
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [root]

        while stack:
            node = stack.pop()

            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            
        return res[::-1]

# Input: root = [1, null, 2, 3]
# Output: [3, 2, 1]

# Input: root = [1]
# Output: [1]

# Input: root = []
# Output: []








        


