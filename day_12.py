
# https://leetcode.com/problems/decompress-run-length-encoded-list/ (easy)
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(0, len(nums), 2):
            res += [nums[i+1]] * nums[i]

        return res


# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent (easy)
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


# https://leetcode.com/problems/sort-vowels-in-a-string (medium)
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U']
        v_in_word = {}
        s = list(s)
        for i in range(0, len(s)):
            if s[i].upper() in vowels:
                v_in_word[i] = s[i]

        v_in_word_vals = sorted(list(v_in_word.values()))
        v_in_word_keys = list(v_in_word.keys())

        for i in range(0, len(v_in_word_vals)):
            s[v_in_word_keys[i]] = v_in_word_vals[i]

        return ''.join(s)

