# https://leetcode.com/problems/truncate-sentence (easy)
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split(' ')[0:k])


# https://leetcode.com/problems/maximum-number-of-coins-you-can-get (medium)
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        total_coins = 0

        for i in range(len(piles) // 3, len(piles), 2):
            total_coins += piles[i]

        return total_coins