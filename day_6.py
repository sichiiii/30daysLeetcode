# https://leetcode.com/problems/minimum-number-game (easy)
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res = []
        nums = sorted(nums)
        for i in range(1, len(nums), 2):
            res.append(nums[i])
            res.append(nums[i - 1])

        return res


# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array (easy)
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digs_sum = 0

        for i in ''.join(str(x) for x in nums):
            digs_sum += int(i)

        return abs(sum(nums) - digs_sum)


# https://leetcode.com/problems/sorting-the-sentence (easy)
class Solution:
    def sortSentence(self, s: str) -> str:
        res = []
        s = s.split(' ')
        count = 1

        while s:
            for i in s:
                if str(count) in i:
                    count += 1
                    res.append(i[:-1])
                    s.remove(i)

        return ' '.join(res)

