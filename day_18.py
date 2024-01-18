# https://leetcode.com/problems/maximum-69-number
class Solution:  # vot eto pizdec
    def maximum69Number(self, num: int) -> int:
        str_num = list(str(num))

        for i in range(0, len(str_num)):
            if str_num[i] == '6':
                str_num[i] = '9'
                break

        return int(''.join(str_num))


# https://leetcode.com/problems/destination-city (easy)
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        res = []

        for i in paths:
            for j in i:
                res.append(j)

        for i in range(1, len(res)):
            el = res[i]
            del res[i]

            if el not in res:
                return el
