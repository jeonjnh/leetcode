class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        arr_needle = list(needle)
        
        for i in range(len(haystack)-len(needle)+1):
            list_haystack = list(haystack[i:i+len(needle)])
            if arr_needle == list_haystack:
                return i
            
        return -1
        
        