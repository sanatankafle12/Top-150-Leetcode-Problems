class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determine if a ransom note can be constructed from a magazine.
        
        This function checks if all characters in the ransom note can be found in the magazine,
        considering the frequency of each character. Each character in the magazine can only
        be used once.
        
        Args:
            ransomNote (str): The ransom note string to construct
            magazine (str): The magazine string containing available characters
            
        Returns:
            bool: True if ransom note can be constructed, False otherwise
            
        Example:
            >>> solution = Solution()
            >>> solution.canConstruct("aa", "ab")
            False
            >>> solution.canConstruct("aa", "aab")
            True
            >>> solution.canConstruct("abc", "abcc")
            True
            
        Time Complexity: O(m + n) where m and n are lengths of magazine and ransomNote
        Space Complexity: O(k) where k is the number of unique characters in magazine
        """
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