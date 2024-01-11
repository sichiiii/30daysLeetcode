# https://leetcode.com/problems/sort-the-students-by-their-kth-score (medium)
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        temp_dict = {}
        res = []

        for i in range(0, len(score)):
            temp_dict[i] = score[i][k]

        temp_dict = dict(sorted(temp_dict.items(), key=lambda item: item[1]))

        for i in reversed(temp_dict.keys()):
            res.append(score[i])

        return res


# https://leetcode.com/problems/partition-array-according-to-given-pivot (medium)
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left_arr = []
        equal_arr = []
        right_arr = []

        for i in nums:
            if i > pivot:
                right_arr.append(i)
            elif i < pivot:
                left_arr.append(i)
            else:
                equal_arr.append(i)

        return left_arr + equal_arr + right_arr
