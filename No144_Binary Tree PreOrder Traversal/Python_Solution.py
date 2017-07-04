# -*- coding: utf-8 -*-
# Renyi Hou.  4/7/2017

题目：
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

解题思路:
基本的思路是递归
PreOrder，先parent val, then left sub-tree, right sub-tree, 

解答：
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        result.append(root.val)
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
        return result
