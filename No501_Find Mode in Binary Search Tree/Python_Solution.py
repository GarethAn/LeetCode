# -*- coding: utf-8 -*-
# Renyi Hou.  27/6/2017
题目：
Given a binary search tree (BST) with duplicates, find all the mode(s) 
(the most frequently occurred element) in the given BST.

解题思路：
对于BST这种数据结构
有三种遍历算法
Pre-order(前序遍历）
In-order（中序遍历） 
Post-order（后序遍历）
本题对BST采取中序遍历，return的是ascending order list
最后，算出order list当中频率最多的element(using collections.Counter)

解答：
本解答当中，midTravse function return the order list
findMode return the most frequently elements 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        result = self.midTraverse(root)
        filter_result = []
        if result is None:
            return filter_result
        if result:
            orderList = collections.Counter(result).most_common(len(set(result)))
            for ele in orderList:
                if ele[1] == orderList[0][1]:
                    filter_result.append(ele[0])
            return filter_result
        return filter_result

        
    def midTraverse(self,root):
        result = []
        if root is None:
            return result
        result.extend(self.midTraverse(root.left))
        result.append(root.val)
        result.extend(self.midTraverse(root.right))
        return result
