# Problem Description: You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.


# class Solution:
#     def findRelativeRanks(self, score: [int]) -> [str]:
#         # Sort scores from highest to lowest
#         sorted_score = sorted(score, reverse = True) 

#         # Map each sorted score to its index
#         score_dict = {score : index for index, score in enumerate(sorted_score)}

#         # Create list of medals in ascending order
#         medals = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(score) + 1)]

#         # Map the score to its corresponding medal
#         result = [medals[score_dict[s]] for s in score]
        
#         return result

class Solution:
    def findRelativeRanks(self, score: [int]) -> [str]:
        # sort the scores from highest to lowest
        sorted_score = sorted(score, reverse = True)

        score_dict = {}
        ans = []

        # gives the medals / placement based on its corresponding position
        for i, s in enumerate(sorted_score):
            if i == 0:
                score_dict[s] = "Gold Medal"
                continue

            if i == 1:
                score_dict[s] = "Silver Medal"
                continue

            if i == 2:
                score_dict[s] = "Bronze Medal"
                continue

            else:
                score_dict[s] = str(i + 1)
        
        for s in score:
            ans.append(score_dict[s]) # append result (based on score_dict with score as key and placement as value)
        
        return ans

# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

# Time complexity: O(n)
# Space complexity: O(1)