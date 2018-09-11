import re
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        res = re.search(needle,haystack)
        if res:
            return res.span()[0]
        else:
            return -1
        
print(Solution().strStr('hello','ll'))
print(Solution().strStr('AAAA','AAB'))
print(Solution().strStr('AAAA',''))



