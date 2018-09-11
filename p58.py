class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        s = s.strip()  #默认删除空白符号（'\r','\n',' '）
        ans = 0
        for si in s[::-1]:
            if si != ' ':
                ans += 1
            else :
                return ans
        return ans

print(Solution().lengthOfLastWord('a '))
print(Solution().lengthOfLastWord('b a '))
print(Solution().lengthOfLastWord(' a'))

