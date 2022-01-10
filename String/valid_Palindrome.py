# Problem Description: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 

        while l <= r:
            while not s[l].isalnum() and l < r: l += 1
            while not s[r].isalnum() and l < r: r -= 1

            if s[l] == s[r] or s[left].upper() == s[right].upper():
                l, r = l + 1, r - 1
            
            else:
                return False

        return True

# Input: s = "A man, a plan, a canal: Panama"
# Output: true 

# Input: s = "race a car"
# Output: false

# Input: s = " "
# Output: true 
