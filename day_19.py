# https://leetcode.com/problems/build-an-array-with-stack-operations (easy)
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []

        for i in range(0, n):
            if i+1 > target[-1]:
                break

            if i+1 in target:
                ops.append('Push')
            else:
                ops.append('Push')
                ops.append('Pop')

        return ops


# https://leetcode.com/problems/decode-xored-array (easy)
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]

        for e in encoded:
            ans.append(e ^ ans[-1])

        return ans