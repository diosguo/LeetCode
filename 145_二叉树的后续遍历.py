# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class RecursionSolution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [] 
        
        return self.postorderTraversal(root.left) + \
            self.postorderTraversal(root.right) + \
            [root.val]

class RecurrentSolution:
    """非递归方式 后序遍历"""
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ... 


        
        

        
