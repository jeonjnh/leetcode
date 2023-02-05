"""
77. Combinations
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
"""
# Runtime 427ms, Beats 56.77%
# Memory 15.9 MB, Beats 46.78%

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(n,k,start,path,res):
            if(len(path) == k):
                res.append(path)
                return None

            for index in range(start, n):
                dfs(n,k,index+1,path+[index+1],res)

        res = []
        dfs(n,k,0,[],res)
        return res
