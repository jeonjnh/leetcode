# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        stack = []
        if root:
            stack.append(root)
        
        while stack:
            size = len(stack)
            level = []
            
            for _ in range(size):
                curr = stack.pop(0)
                level.append(curr.val)
                
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                    
            ans.append(level)
                
            
        return ans