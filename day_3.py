# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points (medium)
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points_sorted = sorted([x for x, y in points])
        max_d = 0
        prev_x = points_sorted[0]
        for i in range(1, len(points_sorted)):
            max_d = max(max_d, points_sorted[i] - prev_x)
            prev_x = points_sorted[i]

        return max_d


# https://leetcode.com/problems/strictly-palindromic-number (medium)
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        bin_n = str(bin(n))

        if len(bin_n) % 2 == 1:
            return False

        while bin_n:
            if bin_n[0] != bin_n[-1]:
                return False
            bin_n = bin_n[1:-1]

        return True