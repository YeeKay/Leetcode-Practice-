# Problem Description: Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashset = set()

        for c in s:
            if c not in hashset:
                hashset.add(c)
            
            else:
                hashset.remove(c)

        # remaining elements in hashset are letters that appear odd number of times 
        # return total number of elements that appear even number of times 
        # otherwise return length of input string if all characters appear even number of times  
        return len(s) -  len(hashset) + 1 if len(hashset) > 0 else len(s)

# Input: s = "abccccdd"
# Output: 7 

# Input: s = "a"
# Output: 1

# Input: s = "bb"
# Output: 2

# Time complexity: O(N)
# Space complexity: O(N)



