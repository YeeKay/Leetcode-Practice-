# Problem Description: Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

# Input: s = "Hello World"
# Output: 5

# Input: s = "   fly me to the moon   "
# Output: 4 

# Input: s = "luffy is still joyboy"
# Output: 6 