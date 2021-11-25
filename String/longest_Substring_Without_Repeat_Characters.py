"Problem description : Given a string s, find the length of the longest substring without repeating characters."

# lengthOfLongestSubstring uses sliding window approach 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        longest_substring = ""

        for char in s:
            if char not in substring:
                substring += char
            
            else:
                # sliding window approach where substring is obtained by dropping duplicating character and appending the new character 
                char_index = substring.find(char)
                substring = substring[char_index + 1: ] + char 
            
            if len(substring) > len(longest_substring):
                longest_substring = substring
        
        return len(longest_substring)


       
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring(""))

# "abcabcbb" -> 3
# "bbbbb" -> 1
# "pwwkew" -> 3
# "" -> 0

# Time complexity : O(n)
# Space complexity : O(1)