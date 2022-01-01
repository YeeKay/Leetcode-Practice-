# Problem Description: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


# Approach 1: Treating the element to be removed as non-existent and keep copying the visible elements in-place in a single pass.  
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 

        for num in nums:
            if num != val:
                nums[i] = val
                i += 1
        
        return i
# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach 2: Two-pointer in place solution
class Solution:
    def removeElement(self, nums:List[int], val: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left], nums[right], right = nums[right], nums[left], right - 1
            
            else:
                left += 1
        
        return left

# Time Complexity: O(n)
# Space Complexity: O(1)

# Input: nums = [3, 2, 2, 3], val = 3
# [2, 2]
# Output: 2, nums = [2, 2, _, _]

# Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
# Output: 5, nums = [0, 1, 3, 0, 4, _, _]