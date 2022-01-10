# Problem Description: Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

pascal_Triangle = [[1]]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        while len(pascal_Triangle) < numRows:
            pascal_Triangle.append(list(map(lambda x, y: x + y, pascal_Triangle[-1] + [0], [0] + pascal_Triangle[-1])))

            # any row can be reconstructed using the offset sum of the previous row 
        
        return pascal_Triangle[:numRows]

# Input: numRows = 5
# Output: [[1], [1, 1], [1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Input: numRows = 1
# Output: [[1]]