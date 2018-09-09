import string
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000}
        dict2 = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        ans = 0
        for strd in dict2:
            if strd in s:
                s = s.replace(strd,'')
                ans += dict2[strd]
        for i in s:
            ans += dict1[i]
        return ans

Solution().romanToInt('XXVII')
Solution().romanToInt('MCMXCIV')
