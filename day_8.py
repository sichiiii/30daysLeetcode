# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words (easy)
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if s == ''.join(i[0] for i in words):
            return True
        return False


# https://leetcode.com/problems/reverse-words-in-a-string-iii (easy)
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(i[::-1] for i in s.split(' '))


# https://leetcode.com/problems/to-lower-case/submissions/ (easy)
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/ (easy)
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if j != i:
                    if abs(nums[i] - nums[j]) == k:
                        count += 1

        return count


# https://leetcode.com/problems/find-center-of-star-graph (easy)
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in edges:
            if edges[0][0] not in i:
                return edges[0][1]
        return edges[0][0]



# https://leetcode.com/problems/count-of-matches-in-tournament (easy)
class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0

        while n > 1:
            if n % 2 == 0:
                count += n // 2
                n -= n // 2
            else:
                count += (n - 1) // 2
                n -= (n - 1) // 2

        return count
