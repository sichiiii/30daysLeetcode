# https://leetcode.com/problems/find-greatest-common-divisor-of-array (easy)
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_div = 1
        max_n = max(nums)
        min_n = min(nums)

        for i in range(1, max(nums) + 1):
            if max_n % i == 0 and min_n % i == 0:
                max_div = i

        return max_div


# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix (easy)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for i in grid:
            for j in i:
                if j < 0:
                    count += 1

        return count


# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences (easy)
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        appearance = {}

        for i in s:
            if i in appearance:
                appearance[i] += 1
            else:
                appearance[i] = 1

        a = appearance[s[0]]

        for value in appearance.values():
            if value != a:
                return False

        return True

