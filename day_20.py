# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string (easy)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            for i in range(0, len(haystack)):
                    if haystack[i] == needle[0]:
                        if haystack[i] + haystack[i+1:i + len(needle)] == needle:
                            return i
        return -1


# https://leetcode.com/problems/removing-stars-from-a-string/ (medium)
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for i in s:
            if i == '*':
                ans.pop()
            else:
                ans.append(i)
        return ''.join(ans)