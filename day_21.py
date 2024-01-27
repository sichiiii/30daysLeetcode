# https://leetcode.com/problems/check-if-the-sentence-is-pangram (easy)
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in 'zyxwvutsrqponmlkjihgfedcba':
            if i not in sentence:
                return False
        return True
