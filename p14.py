class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        fstr = strs[0]
        ans = ''
        for i in fstr:
            strss = []
            for str in strs:
                if str.startswith(i) == False:
                    return ans
                str = str[1:]
                strss.append(str)
            strs = strss
            ans += i
        return ans

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
print(Solution().longestCommonPrefix([]))

