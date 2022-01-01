# Problem Description:
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(nums) != len(set(nums)) else False 
    

# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1, 2, 3, 4]
# Output: false

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Time complexity: O(N)
# Space complexity: O(N)