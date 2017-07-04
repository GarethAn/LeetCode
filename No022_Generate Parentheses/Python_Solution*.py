# -*- coding: utf-8 -*-
# Renyi Hou.  28/6/2017
题目:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

解题思路：
递归思想。
 * 左括号的个数大于等于右括号的个数。所以，我们就可以按照这个规则去打印括号：
 * 假设在位置k我们还剩余left个左括号和right个右括号，如果left>0，则我们可以直接打印左括号，
 * 而不违背规则。能否打印右括号，我们还必须验证left和right的值是否满足规则，如果left>=right，
 * 则我们不能打印右括号，因为打印会违背合法排列的规则，否则可以打印右括号。如果left和right均为零，
 * 则说明我们已经完成一个合法排列，可以将其打印出来。通过深搜，我们可以很快地解决问题，针对n=2，
 * 我对于这句话的理解是：
 首先我们判定，我们在位置k的情况下，我们有n个左括号，m个右括号
 如果n > 0,我们可以直接插入左括号
 
解答：
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
       
    def help(self, remainLeftParenthese, remainRightParenthese, currentItem, results):
        if remainRightParenthese < remainLeftParenthese:#这个condition意味着已经存在的右括号多于已存在的左括号，很显然，这种情况，配对失败
            return
        if remainLeftParenthese: ##如果left>0，则我们可以直接打印左括号
            self.help(remainLeftParenthese - 1, remainRightParenthese, currentItem + '(', results)
        if remainLeftParenthese <= remainRightParenthese:
            self.help(remainLeftParenthese, remainRightParenthese - 1, currentItem + '(', results)
        if remainLeftParenthese == 0 and remainRightParenthese == 0:
            results.append(currentItem)
            
            
        
