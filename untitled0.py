# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 21:56:23 2022

@author: Rakin Shahriar
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = sorted(s)
        list2 = sorted(t)
        return list1 == list2
        
        
        
list_a = "an"
list_b = "na"
t = Solution()
t = t.isAnagram(list_a,list_b)
print("List 1 = ",list_a)
print("List 2 = ",list_b)
print(t)