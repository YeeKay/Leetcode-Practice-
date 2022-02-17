# Problem Description:

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive method
class Solution(object):
    def isBalanced(self, root):
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            if left == -1:
                return -1

            right = check(root.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1
        
        return check(root) != -1

# Time complexity: O(n)
# Space complexity: O(1)

# Iterative method

class Solution:
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right = depths.get(node.left, 0), depths.get(node.right, 0)

                    if abs(left - right) > 1: return False

                    depths[node] = 1 + max(left, right)

                    last = node
                    node = None
                
                else:
                    node = node.right
        
        return True

# Time complexity: O(n)
# Space compleity: O(n)
        
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Input: root = []
# Output: true