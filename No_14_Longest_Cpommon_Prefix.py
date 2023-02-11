"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        res = []
        length = 0
        first, last = strs[0],strs[-1]

        if(len(first) > len(last)):
            length = len(last)
        else:
            length = len(first)

        for i in range(length):
            if(first[i] == last[i]):
                res.append(first[i])
            else:
                return "".join(res)

        return "".join(res)
