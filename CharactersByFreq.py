import operator

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        myMap = {}
        for c in s:
            if c not in myMap:
                myMap[c] = 1
            else:
                myMap[c] += 1
        
        pairs = sorted(myMap.items(), key=operator.itemgetter(1), reverse=True)
        res = ""
        for pair in pairs:
            res += pair[0]*pair[1]
            
        return res