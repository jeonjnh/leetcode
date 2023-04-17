class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        expected = heights.copy()
        
        has_swap = True
        while has_swap:
            has_swap = False
            for i in range(len(expected)-1):
                if expected[i] > expected[i+1]:
                    expected[i],expected[i+1] = expected[i+1],expected[i]
                    has_swap = True
                    
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
                
        return res
        