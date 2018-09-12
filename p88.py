class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1.reverse()
        ks = 0
        while ks != n:
            nums1.remove(0)
            ks += 1
        nums1.extend(nums2)
        nums1.sort()


# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# nums1.extend(nums2)
# while 0 in nums1:
    # nums1.remove(0)
# nums1.sort()
# print(nums1)

print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))

