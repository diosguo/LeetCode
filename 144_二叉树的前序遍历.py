# Definition for a binary tree node.
from typing import Mapping, Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = set() 
        result = []
        queue = [root] 

        while queue:
            p = queue[-1] 

            if p in visited:
                queue.pop(0)
                if p.right:
                    queue.append(p.right)
            else:
                visited.add(p)
                result.append(p.val)
                if p.left:
                    queue.append(p.left)
        return result 


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(0)

    root.left = TreeNode(1)
    root.right = TreeNode(2)

    res = s.preorderTraversal(root)
    print(res)