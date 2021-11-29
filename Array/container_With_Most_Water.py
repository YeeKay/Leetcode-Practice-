# Problem description : Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

# Notice that you may not slant the container.

# maxArea uses two-pointer approach
class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R, width, area = 0, len(height) - 1, len(height) - 1, 0 # initialization 

        for w in range(width, 0, -1):
            if height[L] < height[R]:
                area, L = max(area, height[L] * w), L + 1 # two-pointer approach
            else:
                area, R = max(area, height[R] * w), R - 1 # two-pointer approach
         
        return area

sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(sol.maxArea([1, 1]))
print(sol.maxArea([4, 3, 2, 1, 4]))
print(sol.maxArea([1, 2, 1]))




    


# Input : height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49

# Inpuut : height = [1, 1]
# Output : 1 

# Input : height = [4, 3, 2, 1, 4]
# Output : 16

# Input : height = [1, 2, 1]
# Output : 2

# Time Complexity : O(n)
# Space Complexity : O(1)