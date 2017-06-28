# -*- coding: utf-8 -*-

题目：
Given an integer array with even length, where different numbers in this array represent different kinds of candies. 
Each number means one candy of the corresponding kind. 
You need to distribute these candies equally in number to brother and sister. 
Return the maximum number of kinds of candies the sister could gain.

解题思路:
For given input list -- lst, len(set(lst) represents the different type of element(不同的元素）
len(candies) represents the number of element
case 1:
设想,lst包括了26个elements, 其中有10种kind,那么return result should be 10
因为sister could gain the 13 elements, 这13个元素中就可以包括10种kind element                                                                                    
case 2:
设想,lst包括了26个elements, 其中有15种kind,那么return result should be 13
因为sister could gain the 13 elements, 这13个元素中就可以包括10种kind element
所以说，result与kind and number of element有关                                                                      

解答:                   
class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)), int(len(candies)/2))
