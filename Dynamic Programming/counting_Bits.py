# Problem Description: Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0]

        for i in range(1, n + 1):
            counter.append(counter[i >> 2] + i % 2)
            # i >> 1 == i // 2 (faster to perform bit-shifting)
            # i % 2 - determine its parity 
        
        return counter 

# Time complexity: O(N) - iterate through the range of numbers once
# Space complexity: O(N) - use a n-sized array