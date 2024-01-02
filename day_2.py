from typing import List

# https://leetcode.com/problems/find-words-containing-character (easy)
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []

        for i in range(0, len(words)):
            if x in words[i]:
                result.append(i)

        return result


# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions (medium)
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        while nums:
            to_delete = []
            res.append([])
            for i in nums:
                if i not in res[-1]:
                    res[-1].append(i)
                    to_delete.append(i)

            for i in to_delete:
                nums.remove(i)

        return res



