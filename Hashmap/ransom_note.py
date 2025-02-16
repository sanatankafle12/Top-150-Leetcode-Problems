class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_list = list(ransomNote)
        magazine_list = list(magazine)
        copy_list = list(ransomNote)
        for x in copy_list:
            if x in magazine_list:
                ransom_list.remove(x)
                magazine_list.remove(x)

        if len(ransom_list) == 0:
            return True
        return False