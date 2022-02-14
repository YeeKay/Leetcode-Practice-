# Problem Description: A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

# You are given an array of strings sentences, where each sentences[i] represents a single sentence.

# Return the maximum number of words that appear in a single sentence.

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sentence.split('')) for sentence in sentences)


# Time complexity: O(N)
# Space complexity: O(1)

# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6

# Input: sentences = ["please wait", "continue to fight", "continue to win"]
# Output: 3

# Constraints
# 1 <= sentences.length <= 100
# 1 <= sentences[i].length <= 100