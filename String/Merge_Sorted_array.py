from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge two sorted arrays in-place.
        
        This function merges nums2 into nums1 in-place. nums1 has enough space
        (length >= m + n) to hold additional elements from nums2. The number of
        elements initialized in nums1 and nums2 are m and n respectively.
        
        Args:
            nums1 (List[int]): First sorted array with extra space at the end
            m (int): Number of elements initialized in nums1
            nums2 (List[int]): Second sorted array
            n (int): Number of elements in nums2
            
        Returns:
            None: Modifies nums1 in-place
            
        Example:
            >>> solution = Solution()
            >>> nums1 = [1, 2, 3, 0, 0, 0]
            >>> solution.merge(nums1, 3, [2, 5, 6], 3)
            >>> nums1
            [1, 2, 2, 3, 5, 6]
            
        Time Complexity: O(m + n) - single pass through both arrays
        Space Complexity: O(1) - modifies nums1 in-place
        """
        # TODO: Implement the solution
        pass
