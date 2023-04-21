class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        dic = {}
        
        for i in range(len(arr)):
            dic[arr[i]] = arr[:i]
            
        for key, val in dic.items():
            if key*2 in val:
                return True
            elif key%2 == 0 and key//2 in val:
                return True
            
        return False