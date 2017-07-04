# -*- coding: utf-8 -*-
# Renyi Hou.  4/7/2017

题目：
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

解题思路:
基本的思路是递归
PostOrder，先left sub-tree then right sub-tree, parent val

解答：

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        
        result.extend(self.postorderTraversal(root.left))
        result.extend(self.postorderTraversal(root.right))        
        result.append(root.val)
        return result
