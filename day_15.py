# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies (easy)
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        mc = max(candies)

        for i in candies:
            if i + extraCandies >= mc:
                res.append(True)
            else:
                res.append(False)

        return res


# https://leetcode.com/problems/range-sum-of-bst/ (easy)
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        result = 0

        if root is None:
            return result

        stack = [root]

        while stack:
            curr = stack.pop()

            if curr.val >= L and curr.val <= R:
                result += curr.val

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return result