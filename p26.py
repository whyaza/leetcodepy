class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nownum = nums[0]
        for num in nums[1:]:
            if num != nownum:
                nownum = num
            else:
                nums.remove(num)
        return len(nums)

print(Solution().removeDuplicates([1,1,2]))
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
