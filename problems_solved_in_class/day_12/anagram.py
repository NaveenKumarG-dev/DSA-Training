
from collections import Counter

class Solution:
    def areAnagrams(self, s1, s2):
       # code here
        if len(s1) == len(s2):
            d1 = Counter(s1)
            d2 = Counter(s2)
            
            for i in d1.keys():
                if i not in d2.keys():
                    return False
                if d1[i] != d2[i]:
                    return False
            
            return True
        
        return False