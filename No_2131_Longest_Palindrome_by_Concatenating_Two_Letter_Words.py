"""
2131. Longest Palindrome by Concatenating Two Letter Words

You are given an array of strings words. Each element of words consists of two lowercase English letters.
Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
A palindrome is a string that reads the same forward and backward.

Example 1:
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
"""

from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        answer = 0
        center = False
        counter = Counter(words)

        for word, cnt in counter.items():
            if(word[0] == word[1]):
                if cnt % 2 == 0:
                    answer += cnt
                else:
                    answer += cnt - 1
                    center = True

            elif(word[0] < word[1]):
                answer += min(cnt,counter[word[1]+word[0]]) * 2

        if center:
            answer += 1
        
        return answer*2



