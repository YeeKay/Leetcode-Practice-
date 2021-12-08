# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Instead of slicing an array recursively and passing them which could be expensive (O(n))
# it is better to pass the left and right bounds into recursive calls instead (O(n))

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums: List[int], lower: int, upper: int) -> Optional[TreeNode]:
        if lower == upper:
            return None
        
        mid = (lower + upper) // 2 

        node = TreeNode(nums[mid])
        node.left = self.helper(nums, lower, mid - 1) # pass left index and right index instead 
        node.right = self.helper(nums, mid + 1, upper)
        return node
        

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]

# Input: nums = [1,3]
# Output: [3,1]

# Time complexity : O(log n)
# Space complexity : O(log n)