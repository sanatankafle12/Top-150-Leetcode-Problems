class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}

        for elements in magazine:
            if elements not in dictionary:
                dictionary[elements] =  1
            else:
                dictionary[elements] += 1

        for elements in ransomNote:
            if elements in dictionary and dictionary[elements]>0:
                dict[elements] -=1
            else:
                return False
        
        return True