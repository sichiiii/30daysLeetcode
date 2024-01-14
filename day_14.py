# https://leetcode.com/problems/matrix-diagonal-sum/ (easy)
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        count = 0
        len_mat = len(mat)

        for i in range(0, len_mat):
            res += mat[i][count] + mat[i][len_mat - 1 - count]
            count += 1

        if len_mat % 2 != 0:
            return res - mat[len_mat // 2][len_mat // 2]
        else:
            return res


# https://leetcode.com/problems/design-parking-system (easy)
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 3:
            if self.small - 1 > -1:
                self.small -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium - 1 > -1:
                self.medium -= 1
                return True
            else:
                return False
        elif carType == 1:
            if self.big - 1 > -1:
                self.big -= 1
                return True
            else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)