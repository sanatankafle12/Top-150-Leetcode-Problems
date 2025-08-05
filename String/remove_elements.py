from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of a given value from an array in-place.
        
        This function modifies the input array by removing all instances of the target value
        and returns the new length of the array. The order of elements may be changed.
        
        Args:
            nums (List[int]): Input array of integers
            val (int): The value to remove from the array
            
        Returns:
            int: The new length of the array after removing all occurrences of val
            
        Example:
            >>> solution = Solution()
            >>> nums = [3, 2, 2, 3]
            >>> solution.removeElement(nums, 3)
            2
            >>> nums[:2]  # First 2 elements after removal
            [2, 2]
            
        Time Complexity: O(n) where n is the length of nums
        Space Complexity: O(1) - modifies array in-place
        """
        len_nums = len(nums)
        count = 0

        i =0

        while(i < len(nums)):
            if (nums[i] == val):
                nums.pop(i)
                nums.insert(len(nums), '_')
                count += 1
            else:
                i+=1
        return(len(nums)-count)