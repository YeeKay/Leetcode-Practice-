# Problem description : Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key : index, value : target - num (diff)
        diff_dict = {} 
        
        for idx, num in enumerate(nums):
            diff = target - num
            try:
                if  diff_dict[num] == 0 or diff_dict[num]:
                    return [diff_dict[num], idx]

            except KeyError: # diff not in dictionary yet
                diff_dict[diff] = idx 

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 3], 6))

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

# Input: nums = [3, 3] target = 6
# Output: [0, 1]


# Time complexity : O(n)
# Space complexity: O(n)