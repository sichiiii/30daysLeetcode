# https://leetcode.com/problems/add-binary (easy)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target (easy)
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
        return count


# https://leetcode.com/problems/left-and-right-sum-differences (easy)
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = []
        left_nums = []
        right_nums = []
        buffer = 0

        for i in range(len(nums)):
            buffer += nums[i]
            left_nums.append(buffer)

        buffer = 0

        for i in range(len(nums) - 1, -1, -1):
            buffer += nums[i]
            right_nums.append(buffer)

        right_nums = right_nums[::-1]

        for i in range(len(nums)):
            left_sum = left_nums[i-1] if i-1 >= 0 else 0
            right_sum = right_nums[i+1] if i+1 < len(nums) else 0
            res.append(abs(left_sum - right_sum))

        return res


# https://leetcode.com/problems/reducing-dishes (hard)
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction, reverse=True)
        res = 0
        prefix_sum = 0

        for i in range(len(satisfaction)):
            prefix_sum += satisfaction[i]

            if prefix_sum < 0:
                break

            res += prefix_sum

        if res < 0:
            return 0

        return res