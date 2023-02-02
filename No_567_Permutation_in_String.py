"""
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        char_s1 = Counter(s1)
        char_diff = Counter()

        for i in range(s2_len - s1_len + 1):
            for j in range(i,i+s1_len):
                r = s2[j]
                char_diff[r] += 1
            if(char_s1 == char_diff):
                return True
            char_diff = Counter()

        return False
