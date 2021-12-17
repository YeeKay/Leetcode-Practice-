# Problem Description: You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))


# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6

# Input: accounts = [[1, 5], [7, 3], [3, 5]]
# Output: 10

# Input: accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
# Output: 17