# -*- coding: utf-8 -*-
# Renyi Hou.  24/6/2017
题目：
Invert a binary tree.

解题思路:
基本的思路是递归

解答：
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def invertTree(self, root):
        """
        :python self的意思是类的实例 (the instance of class)
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        root.left, root.right = root.right,root.left
        # above is a standard method that swap two variable values in Python
        return root
        
Tips:
Python语言当中，self表示instance of the class
在class Solution中，self表示instance of the Soluction
所以说如果要调用Solution中的invertTree，需要self.inverTree(argument)
