# https://leetcode.com/problems/remove-element/ (easy)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[count] = nums[i] 
                count += 1

        return count


# https://leetcode.com/problems/find-the-maximum-achievable-number/ (easy)
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return 2 * t + num


# https://leetcode.com/problems/find-the-original-array-of-prefix-xor (medium)
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        for i in range(1, len(pref)):
            ans.append(pref[i] ^ pref[i - 1])

        return ans

