# -*- coding: utf-8 -*-
# Renyi Hou.  26/6/2017
题目:
Find the sum of all left leaves in a given binary tree.

解题思路：
递归思想。在一开始的时候，如果left tree没有left and right tree，那么这个node判定为left leave

解答：
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        if root:
            l, r = root.left, root.right
            #if l and (not l.right) and (not l.left):
            #if l and (l.right or l.left) is None: #比如l.right存在，l.left不存在，那么(l.right or l.left)就是l.right, 所以这句话（l.right or l.left) is None相当于希望判定（l.right is None) and (l.left is None)
            if l and (l.right is None) and (l.left is None):
                ans += l.val
            ans += self.sumOfLeftLeaves(l) + self.sumOfLeftLeaves(r)
        else:
            return 0
        return ans
                
