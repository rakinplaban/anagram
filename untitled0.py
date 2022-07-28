# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 21:56:23 2022

@author: Rakin Shahriar
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = Counter(s)
        s2 = Counter(t)
        list1,list2 = [],[]
        
        for i in s1:
            list1.append(i)
            
        list1.sort()
            
        for i in s2:
            list2.append(i)
        list2.sort()
        
        flag = 0
            
        if len(list1) <= len(list2):
            for i in range(len(list1)):
                #for j in range(len(list2)):
                if list1[i] not in list2:
                    flag = 1
                
        else:
            for i in range(len(list2)):
                #for j in range(len(list2)):
                if list2[i] not in list1:
                    flag = 1
                    
        if flag == 0:
            return True
                
        else:
            return False
        
        
list_a = "b"
list_b = "rat"
t = Solution()
t = t.isAnagram(list_a,list_b)
print(t)