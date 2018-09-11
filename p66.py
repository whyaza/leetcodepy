class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        isJ = True
        ans = []
        for di in digits[::-1]:
            if isJ:
                if di == 9:
                    ans.append(0)
                else:
                    ans.append(di+1)
                    isJ = False
            else:
                ans.append(di)
        if isJ:
            ans.append(1)
        ans.reverse()
        return ans

print(Solution().plusOne([9]))




