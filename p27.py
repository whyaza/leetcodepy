class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while nums.count(val):
            nums.remove(val)
        return len(nums)

print(Solution().removeElement([3,2,2,3],2))
