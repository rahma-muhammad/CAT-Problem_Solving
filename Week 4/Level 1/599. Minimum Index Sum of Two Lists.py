from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = dict(enumerate(list1))
        min = len(list1) * 2 if len(list1)>len(list2) else len(list2) * 2
        res = []
        for i , n in enumerate(list2):
            if n in dict1.values():
                if (i + list(dict1.keys())[list(dict1.values()).index(n)]) < min:
                    res.clear()
                    res.append(n)
                    min = abs(i + list(dict1.keys())[list(dict1.values()).index(n)])
                elif (i + list(dict1.keys())[list(dict1.values()).index(n)]) == min:
                    res.append(n)
                    
        return res

t = Solution()
print(t.findRestaurant(["happy","sad","good"],["sad","happy","good"])) #sad, happy
print(t.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Burger King","Tapioca Express","Shogun"]))