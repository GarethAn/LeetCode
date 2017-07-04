# -*- coding: utf-8 -*-
# Renyi Hou.  4/7/2017

题目：
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

解题思路:
基本的思路是递归
中序遍历，就是把BST transfer to the order list

解答：

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result

可能会碰到的错误：
之前写代码的时候，忘记在line41添加return result
会导致程序“'NoneType' object is not iterable”，因为程序不停的递归，到最后没有东西返回，自然not iterable
