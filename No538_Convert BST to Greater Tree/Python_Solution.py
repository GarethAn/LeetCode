# -*- coding: utf-8 -*-
# Renyi Hou.  4/7/2017
题目：
Given a Binary Search Tree (BST), convert it to a Greater Tree such that 
every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

解题思路:
基本的思路是递归

一开始的思路是，把bst 用inorder traversal转化为list，然后取比node val大的一段list的和，与本身val相加。



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
       
    def 
