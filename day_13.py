# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array (easy)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)

        return (max1 - 1) * (max2 - 1)


# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array (middle)
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        return max(nums[i] + nums[len(nums) - 1 - i] for i in range(len(nums) // 2))
