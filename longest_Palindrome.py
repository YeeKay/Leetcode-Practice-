" Problem description : Given a string s, return the longest palindromic substring in s."

class Solution:
    " Finds all palindromes"
    def findPalindrome(self, s : str, low : int, high : int) -> str:
        length  = len(s)

        # expand from center by decrementing low index by 1 and incrementing high index by 1
        while low >= 0 and high < len(s) and s[low] == s[high]:
            low -= 1
            high += 1

        # undo the center expanding operation
        low += 1
        high -= 1

        if s[low] == s[high]:
            return s[low : high + 1] # return palindrome substring 

    def longestPalindrome(self, s : str) -> str:
        longestPalindrome = "" 
        length = len(s)
        
        # return empty string or the input string as it is 
        if length == 0 or length == 1:
            return s

        for i in range(1, length):
            # generate all even-length palindromes 
            low = i - 1
            high = i 

            evenPalindrome = self.findPalindrome(s, low, high) 
            
            # updates longest palindrome found 
            if evenPalindrome and len(evenPalindrome) > len(longestPalindrome):
                longestPalindrome = evenPalindrome

            # generate all odd-length palindrome 
            low = i - 1 
            high = i + 1 

            oddPalindrome = self.findPalindrome(s, low, high)

            # updates longest palindrome found 
            if oddPalindrome and len(oddPalindrome) > len(longestPalindrome):
                longestPalindrome = oddPalindrome
            
        return longestPalindrome

sol = Solution()
print(sol.longestPalindrome(""))
print(sol.longestPalindrome("a"))
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("ac"))

# "" -> ""
# "a" -> "a"
# "babad" -> "bab"
# "cbbd" -> "bb"
# "ac" -> "c"

# Time complexity : O(n^2)
# Space complexity : O(1)

