from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix among an array of strings.
        
        This function finds the longest common prefix string amongst an array of strings.
        If there is no common prefix, it returns an empty string.
        
        Args:
            strs (List[str]): Array of strings to find common prefix
            
        Returns:
            str: The longest common prefix, or empty string if no common prefix exists
            
        Example:
            >>> solution = Solution()
            >>> solution.longestCommonPrefix(["flower", "flow", "flight"])
            "fl"
            >>> solution.longestCommonPrefix(["dog", "racecar", "car"])
            ""
            >>> solution.longestCommonPrefix(["interspecies", "interstellar", "interstate"])
            "inters"
            >>> solution.longestCommonPrefix(["a"])
            "a"
            
        Time Complexity: O(S) where S is the sum of all characters in all strings
        Space Complexity: O(1) - uses constant extra space
        """
        str_len = [len(str) for str in strs]    
        min_ = min(str_len)
        max = 0
        for i in range(1,min_+1):
            x = [str[:i] for str in strs]
            if len(set(x)) == 1 and max <= i:
                max = i
                continue
        return(strs[0][:max])
