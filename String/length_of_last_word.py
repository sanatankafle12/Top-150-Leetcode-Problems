class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Find the length of the last word in a string.
        
        This function returns the length of the last word in the given string.
        A word is defined as a maximal substring consisting of non-space characters.
        The string may contain leading or trailing spaces.
        
        Args:
            s (str): Input string containing words separated by spaces
            
        Returns:
            int: Length of the last word in the string
            
        Example:
            >>> solution = Solution()
            >>> solution.lengthOfLastWord("Hello World")
            5
            >>> solution.lengthOfLastWord("   fly me   to   the moon  ")
            4
            >>> solution.lengthOfLastWord("luffy is still joyboy")
            6
            >>> solution.lengthOfLastWord("   ")
            0
            
        Time Complexity: O(n) where n is the length of the string
        Space Complexity: O(n) due to string splitting operation
        """
        return(len(s.split()[-1]))