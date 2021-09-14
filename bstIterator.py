# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stacks = []
        self.dfs(root)
    def dfs(self, root):
        while(root is not None):
            self.stacks.append(root)
            root = root.left
        

    def next(self):
        """
        :rtype: int
        """
        newroot = self.stacks.pop()
        self.dfs(newroot.right)
        return newroot.val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stacks) > 0:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
