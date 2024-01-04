# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference (easy)
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum = 0

        for i in range(1, n + 1):
            if i % m:
                sum += i
            else:
                sum -= i

        return sum


# https://leetcode.com/problems/number-of-employees-who-met-the-target (easy)
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0

        for i in hours:
            if i >= target:
                count += 1

        return count
