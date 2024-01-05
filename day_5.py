# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/ (easy)
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        counter = 0

        for i in range(0, len(nums)):
            if i.bit_count() == k:
                counter += nums[i]

        return counter


# https://leetcode.com/problems/number-of-laser-beams-in-a-bank (medium)
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        prev_con = bank[0].count('1')
        for i in range(1, len(bank)):
            mult = prev_con * bank[i].count('1')
            count += mult

            if bank[i].count('1') != 0:
                prev_con = bank[i].count('1')

        return count



