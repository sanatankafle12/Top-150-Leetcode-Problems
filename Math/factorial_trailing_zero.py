class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Count the number of trailing zeroes in n! (n factorial).
        
        This function calculates the number of trailing zeroes in the factorial
        of a given number. Trailing zeroes are created by factors of 10, which
        come from pairs of 2 and 5. Since there are always more factors of 2
        than 5, we only need to count factors of 5.
        
        Args:
            n (int): A non-negative integer (0 <= n <= 10^4)
            
        Returns:
            int: Number of trailing zeroes in n!
            
        Example:
            >>> solution = Solution()
            >>> solution.trailingZeroes(3)
            0
            >>> solution.trailingZeroes(5)
            1
            >>> solution.trailingZeroes(10)
            2
            >>> solution.trailingZeroes(25)
            6
            
        Time Complexity: O(log n) - we divide by 5, 25, 125, etc.
        Space Complexity: O(1) - uses only constant extra space
        """
        # TODO: Implement the solution
        pass
