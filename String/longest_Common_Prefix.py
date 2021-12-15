# Problem Description: Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs:[str]) -> str:
        if not strs: 
            return ""
        
        shortest = min(strs) # return minimum alphabetically-sorted string 
        longest = max(strs) # return maximum alphabetically-sorted string

        for index, char in enumerate(shortest):
            if char != longest[index]: 
                return shortest[:index] # return longest common prefix
        
        return shortest


# class Solution:
#     def longestCommonPrefix(self, strs:[str]) -> str:
#         if not strs:
#             return ""
#         shortest = min(strs, key = len)

#         for i, ch in enumerate(shortest):
#             for others in strs:
#                 if others[i] != ch:
#                     return shortest[:i]
#         return shortest


# Input: strs = ["flo", "flight", "flowers"]
# Output: "fl"

# Input: strs = ["dog", "racecar", "car"]
# Output: ""

# Time complexity: O(n)
# Space complexity: O(1)




                

