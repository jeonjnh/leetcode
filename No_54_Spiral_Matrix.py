"""
https://leetcode.com/problems/spiral-matrix/?envType=study-plan&id=level-2

54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""
# Runtime 27 ms Beats 92.3%
# Memory 13.9 MB Beats 76.17%

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        left,right = 0, len(matrix[0])
        top,bottom = 0, len(matrix)
        while left < right and top < bottom:
            for i in range(left,right):
                res.append(matrix[top][i])
            
            top += 1
            
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            
            right -= 1
            
            if not (left < right and top < bottom):
                break

            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            
            bottom -= 1
            
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            
            left += 1        
                

        return res
