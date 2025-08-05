class Solution:
    def plusOne(self, digits):
        """
        Add one to a number represented as an array of digits.
        
        This function takes an array representing a non-negative integer and returns
        an array representing that integer plus one. The digits are stored such that
        the most significant digit is at the head of the list.
        
        Args:
            digits (List[int]): Array of digits representing a non-negative integer
            
        Returns:
            List[int]: Array of digits representing the input number plus one
            
        Example:
            >>> solution = Solution()
            >>> solution.plusOne([1, 2, 3])
            [1, 2, 4]
            >>> solution.plusOne([9, 9])
            [1, 0, 0]
            >>> solution.plusOne([0])
            [1]
            
        Time Complexity: O(n) where n is the number of digits
        Space Complexity: O(n) in worst case when carry propagates to new digit
        """
        num_str =''
        for i in digits:
            num_str+=str(i)
        
        string_list = list(str(int(num_str)+1))    
        return ([int(x) for x in string_list])