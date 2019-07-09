# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        from queue import Queue
        queue = Queue()
        queue.put(root)
        level_sp = root
        level_last = None
        res = []
        leve_res = []
        while not queue.empty():

            t = queue.get()

            leve_res.append(t.val)
            print(leve_res)
            if t.left:
                queue.put(t.left)
                level_last = t.left
            if t.right:
                queue.put(t.right)
                level_last = t.right

            if t == level_sp:
                res.append(leve_res)
                level_sp = level_last
        res.reverse()
        return res


root = TreeNode(3)
s = Solution()
res = s.levelOrderBottom(root)
print(res)