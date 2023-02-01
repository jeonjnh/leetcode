"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring s without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""
# Sliding Window

from collections import Counter 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        slen = len(s)
        chars = Counter()
        result = 0
        while(right < slen):
            r = s[right]
            chars[r] += 1
            while(chars[r] > 1):
                l = s[left]
                chars[l] -= 1
                left += 1

            result = max(result, right-left+1)
            right += 1

        return result
