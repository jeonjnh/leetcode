class Solution:
    def reverse(self, x: int) -> int:

        minus = False
        
        if x < 0:
            x = abs(x)
            minus = True

        y = 0
        while x > 0:
            d = x % 10
            y = y*10 + d
            x = x // 10
            
        if minus:
            y = y * -1
            
        if y >= 2**31-1 or y <= -2**31:
            return 0
            
        return y