class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
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