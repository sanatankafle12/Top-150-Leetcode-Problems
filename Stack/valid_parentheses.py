class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if a string of parentheses is valid.
        
        This function checks if the input string has valid parentheses. A string is valid if:
        - Open brackets must be closed by the same type of brackets
        - Open brackets must be closed in the correct order
        - Every close bracket has a corresponding open bracket of the same type
        
        Args:
            s (str): String containing only the characters '(', ')', '{', '}', '[' and ']'
            
        Returns:
            bool: True if the string is valid, False otherwise
            
        Example:
            >>> solution = Solution()
            >>> solution.isValid("()")
            True
            >>> solution.isValid("()[]{}")
            True
            >>> solution.isValid("(]")
            False
            >>> solution.isValid("([)]")
            False
            >>> solution.isValid("{[]}")
            True
            
        Time Complexity: O(n) where n is the length of the string
        Space Complexity: O(n) in worst case when all characters are opening brackets
        """
        parentheses_dictionary = {")":"(", "}":"{", "]":"["}

        stack_of_parentheses = []

        for i in s:
            if i in parentheses_dictionary.values():
                stack_of_parentheses.append(i)
            elif i in parentheses_dictionary.keys():
                if not stack_of_parentheses or parentheses_dictionary[i] != stack_of_parentheses.pop():
                    return False
                
        return True