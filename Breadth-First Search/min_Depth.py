# Problem Description: Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution: 
    def minDepth(self, root):
        if not root:
            return 0 
        
        depth = 0
        current_level = [root] # BFS exploration

        while current_level:
            depth += 1
            next_level = []
            
            for node in current_level:
                left, right = node.left, node.right 

                if not left and not right: # leaf node
                    return depth
                
                if left:
                    next_level.append(left)
                
                if right:
                    next_level.append(right)
            
            current_level = next_level 
        
        return depth

# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5               

# Time Complexity: O(log n)
# Space Complexity: O(1)

