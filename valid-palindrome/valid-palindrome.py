class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s.lower()
        s_new = ""
        
        for char in s:
            if char.isalnum():
                s_new = s_new + char.lower()
            
        return True if s_new[:].lower() == s_new[::-1].lower() else False
        